# mainapp/tests.py
from django.test import TestCase, Client
from django.urls import reverse
import json

class GetResponseViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('get_response') #'get_response'의 경로 저장

    def test_get_response_success(self):
        # 올바른 POST 요청으로 성공적인 응답을 받는지 테스트
        response = self.client.post(
            self.url,
            data=json.dumps({'message': '안녕하세요'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.json())
        # 모델 연결하기 전, 임시 답변 테스트 모델 연결 이후에는 주석처리 
        self.assertEqual(response.json().get('response'), '답안녕하세요')

    def test_get_response_invalid_method(self):
        # GET 요청으로 접근할 경우 에러 응답을 받는지 테스트
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_get_response_invalid_json(self):
        # 잘못된 JSON 데이터를 보냈을 때 에러를 받는지 테스트
        response = self.client.post(
            self.url,
            data='Invalid JSON',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())