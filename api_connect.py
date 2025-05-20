def send_to_gpt(mesaj):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Zekabot'un kontrol motorusun. Gelen verileri analiz et."},
                {"role": "user", "content": mesaj}
            ]
        )
        yanit = response.choices[0].message.content
        model_adi = response.model  # kullanılan modeli alıyoruz
        return f"Yanıt: {yanit}\nModel: {model_adi}"
    except Exception as e:
        return f"GPT Hatası: {str(e)}"
