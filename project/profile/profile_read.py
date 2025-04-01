import mammoth
import re
import json
from typing import Dict, List
from pathlib import Path

class ResumeConverter:
    def __init__(self, file_path: str):
        """
        Word履歴書をWeb形式に変換するコンバーターを初期化
        
        :param file_path: Wordドキュメントのパス
        """
        self.file_path = file_path
        self.resume_content = self._extract_text()
        self.parsed_sections = {}

    def _extract_text(self) -> str:
        """
        Wordドキュメントからテキストを抽出
        
        :return: 抽出されたテキスト
        """
        try:
            with open(self.file_path, "rb") as docx_file:
                result = mammoth.extract_raw_text(docx_file)
                return result.value
        except Exception as e:
            print(f"ファイル読み取りエラー: {e}")
            return ""

    def parse_resume(self) -> Dict[str, List[str]]:
        """
        テキストから履歴書のセクションを解析
        
        :return: パースされた履歴書のセクション
        """
        # セクション識別用の正規表現パターン
        sections = {
            'personal_info': r'(名前|氏名|連絡先)',
            'education': r'(学歴|教育|Education)',
            'work_experience': r'(職歴|職務経歴|Work Experience)',
            'skills': r'(スキル|技術|Skills)'
        }

        # セクション初期化
        parsed_sections = {
            'personal_info': [],
            'education': [],
            'work_experience': [],
            'skills': []
        }

        # テキストを行に分割
        lines = self.resume_content.split('\n')
        current_section = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # セクション判定
            for section, pattern in sections.items():
                if re.search(pattern, line, re.IGNORECASE):
                    current_section = section
                    break

            # 各セクションに行を追加
            if current_section and line:
                parsed_sections[current_section].append(line)

        self.parsed_sections = parsed_sections
        return parsed_sections

    def generate_html_resume(self) -> str:
        """
        パースされた履歴書からHTML形式のレジュメを生成
        
        :return: HTML形式の履歴書
        """
        html = f"""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Web履歴書</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #333; border-bottom: 2px solid #333; }}
        h2 {{ color: #666; margin-top: 20px; }}
        .section {{ margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="resume">
        <h1>{self.parsed_sections['personal_info'][0] if self.parsed_sections['personal_info'] else 'Unnamed'}</h1>
        
        <div class="section">
            <h2>連絡先情報</h2>
            <p>{' | '.join(self.parsed_sections['personal_info'][1:]) if len(self.parsed_sections['personal_info']) > 1 else 'No contact information'}</p>
        </div>
        
        <div class="section">
            <h2>学歴</h2>
            <ul>
                {''.join(f'<li>{edu}</li>' for edu in self.parsed_sections['education'])}
            </ul>
        </div>
        
        <div class="section">
            <h2>職歴</h2>
            <ul>
                {''.join(f'<li>{job}</li>' for job in self.parsed_sections['work_experience'])}
            </ul>
        </div>
        
        <div class="section">
            <h2>スキル</h2>
            <ul>
                {''.join(f'<li>{skill}</li>' for skill in self.parsed_sections['skills'])}
            </ul>
        </div>
    </div>
</body>
</html>
        """
        return html

    def save_html_resume(self, output_path: str = 'resume.html'):
        """
        HTMLの履歴書を指定されたパスに保存
        
        :param output_path: 出力するHTMLファイルのパス
        """
        html_content = self.generate_html_resume()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"履歴書をHTML形式で {output_path} に保存しました。")

def main():
    file_path = Path("project/profile/file/resume.docx")
    # 使用例
    try:
        # Wordファイルのパスを指定
        converter = ResumeConverter(file_path)
        
        # 履歴書をパース
        parsed_sections = converter.parse_resume()
        
        # JSONとして出力（オプション）
        print(json.dumps(parsed_sections, ensure_ascii=False, indent=2))
        
        # HTMLに変換して保存
        converter.save_html_resume('web_resume.html')
    
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()