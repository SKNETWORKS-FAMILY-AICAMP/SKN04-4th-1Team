# mainapp/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from bs4 import BeautifulSoup
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

class ChatbotViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chat_view_response(self):
        # 1.1 chat 페이지를 가져온다.
        response = self.client.get('')
        
        # 1.2 정상적으로 페이지가 로드된다.
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        # 1.3 페이지의 타이틀은 📚 Enco Library Chatbot이다.
        self.assertEqual(soup.title.text, '📚 Enco Library Chatbot')

        # 1.4 헤더가 있다.
        header = soup.header
        
        # 1.5 📚 Enco Library라는 문구가 헤더에 있다.
        self.assertIsNotNone(header)
        self.assertIn('📚 Enco Library', header.text)

        # 1.6 메시지를 입력할 수 있는 input_field가 있다.
        input_field = soup.find('input', {'id': 'user-input'})
        
        # 1.7 질문 양식이 input_field에 있다.
        self.assertIsNotNone(input_field)
        self.assertEqual(
            input_field['placeholder'],
            '질문양식: 제목이 {제목}인 책에 대해서 알려줘// {제목} 책을 알려줘// 작가의 이름이 {작가이름}인 책을 알려줘 // {키워드}에 대한 책을 알려줘'
        )

        # 1.8 버튼이 있다.
        button = soup.find('button', {'onclick': 'sendMessage()'})
        
        # 1.9 전송이라는 문구가 button에 있다.
        self.assertIsNotNone(button)
        self.assertEqual(button.text, '전송')

