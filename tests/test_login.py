from bili_game_sdk.api import (
    external_issue_cipher_v3,
    external_login_v3,
    client_activate,
)


if __name__ == "__main__":
    user_id = "your account"
    password = "your password"
    # bd_id
    bd_id = client_activate()
    if bd_id is not None:
        cipher_info = external_issue_cipher_v3()
        # login
        login_response = external_login_v3(
            user_id=user_id, password=password, cipher_info=cipher_info, bd_id=bd_id
        )
        print(login_response)
