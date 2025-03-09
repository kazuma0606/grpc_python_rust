use tonic::{transport::Server, Request, Response, Status};
use chrono::Utc;

pub mod test {
    tonic::include_proto!("grpcetst");
}

use test::test_service_server::{TestService, TestServiceServer};
use test::{TestRequest, TestResponse};

#[derive(Debug, Default)]
pub struct MyTestService {}

#[tonic::async_trait]
impl TestService for MyTestService {
    async fn test_method(
        &self,
        request: Request<TestRequest>,
    ) -> Result<Response<TestResponse>, Status> {
        println!("Requiest from {:?}", request.remote_addr());

        let req = request.into_inner();
        let now = Utc::now().to_rfc3339();

        let response = TestResponse {
            name: req.name,
            email: req.email,
            password: req.password,
            created_at: now.clone(),
            updated_at: now,
        };

        Ok(Response::new(response))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "127.0.0.1:50051".parse()?;
    let test_service = MyTestService::default();

    Server::builder()
        .add_service(TestServiceServer::new(test_service))
        .serve(addr)
        .await?;

    Ok(())
}