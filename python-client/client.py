# client.pyの修正版
import grpc
import test_pb2
import test_pb2_grpc
import time

def run():
    # サーバーへの接続を少し遅延させる
    time.sleep(1)
    
    # localhost（IPv4）を使用
    channel = grpc.insecure_channel('127.0.0.1:50051')
    
    # スタブの作成
    stub = test_pb2_grpc.TestServiceStub(channel)
    
    # リクエストの作成
    request = test_pb2.TestRequest(
        name="テストユーザー",
        email="test@example.com",
        password="password123"
    )
    
    try:
        # サービスの呼び出し
        response = stub.TestMethod(request)
        print("gRPC 呼び出し成功!")
        print(f"名前: {response.name}")
        print(f"メール: {response.email}")
        print(f"パスワード: {response.password}")
        print(f"作成日時: {response.created_at}")
        print(f"更新日時: {response.updated_at}")
    except grpc.RpcError as e:
        print(f"エラーが発生しました: {e.code()} - {e.details()}")
    finally:
        channel.close()

if __name__ == '__main__':
    run()