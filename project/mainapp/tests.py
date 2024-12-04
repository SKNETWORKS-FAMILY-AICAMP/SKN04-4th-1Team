from django.test import TestCase, Client
from bs4 import BeautifulSoup
from django.urls import reverse

class ChatbotViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_chat_view_response(self):
        # 1.1 chat 페이지를 가져온다.
        response = self.client.get('/chat/')
        
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
            '질문양식: 제목이 {제목}인 책에 대해서 알려줘 {작가이름} 작가의 책을 알려줘 {분야} 책을 알려줘'
        )

        # 1.8 버튼이 있다.
        button = soup.find('button', {'onclick': 'sendMessage()'})
        
        # 1.9 전송이라는 문구가 button에 있다.
        self.assertIsNotNone(button)
        self.assertEqual(button.text, '전송')
