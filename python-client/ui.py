import streamlit as st
import grpc
import test_pb2
import test_pb2_grpc

st.title("gRPC Test Client")

# フォーム入力
with st.form("grpc_form"):
    name = st.text_input("名前", value="テストユーザー")
    email = st.text_input("メールアドレス", value="test@example.com")
    password = st.text_input("パスワード", value="password123", type="password")
    
    submitted = st.form_submit_button("送信")
    
    if submitted:
        # リクエスト送信
        try:
            with grpc.insecure_channel('127.0.0.1:50051') as channel:
                stub = test_pb2_grpc.TestServiceStub(channel)
                
                request = test_pb2.TestRequest(
                    name=name,
                    email=email,
                    password=password
                )
                
                response = stub.TestMethod(request)
                
                # 結果表示
                st.success("gRPC呼び出し成功!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("リクエスト")
                    st.write(f"名前: {name}")
                    st.write(f"メール: {email}")
                    st.write(f"パスワード: {'*' * len(password)}")
                
                with col2:
                    st.subheader("レスポンス")
                    st.write(f"名前: {response.name}")
                    st.write(f"メール: {response.email}")
                    st.write(f"パスワード: {response.password}")
                    st.write(f"作成日時: {response.created_at}")
                    st.write(f"更新日時: {response.updated_at}")
                    
        except grpc.RpcError as e:
            st.error(f"エラーが発生しました: {str(e)}")