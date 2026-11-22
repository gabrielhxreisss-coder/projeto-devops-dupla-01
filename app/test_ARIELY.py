from app import app

def test_aluno_responde_200():
    assert app.test_client().get("/aluno").status_code == 200