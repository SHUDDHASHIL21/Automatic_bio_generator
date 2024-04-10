from flask import Flask, request, jsonify
import re
import random

app = Flask(__name__)

generated_bios = set()
MAX_BIOS = 25  

def process_input(value):
    return '' if value.lower() == 'null' else value

@app.route('/generate_bio', methods=['POST'])
def generate_bio():
    try:
        data = request.json

        full_name = process_input(data.get('name', ''))
        gender = process_input(data.get('gender', ''))
        marital_status = process_input(data.get('marital_status', ''))
        interests = process_input(data.get('interests', ''))
        profession = process_input(data.get('profession', ''))
        religion = process_input(data.get('religion', ''))

        first_name_match = re.match(r'^\s*([A-Za-z]+)\s*', full_name)
        if first_name_match:
            first_name = first_name_match.group(1)
        else:
            first_name = ''

        bio_templates = [
            
            f"Hey there! I'm {first_name}, a {gender.lower() if gender else 'person'} looking for a meaningful connection. I have a keen interest in {interests.lower() if interests else 'various activities'} and cherish the principles of {religion.lower() if religion else 'life'}. Searching for someone who shares similar values and dreams.",
            f"Greetings! I'm {first_name}, {marital_status.lower()} {gender.lower() if gender else 'person'} in the field of {profession.lower() if profession else 'work'}, exploring the world of {interests.lower() if interests else 'various activities'}. I enjoy various activities and follow the principles of {religion.lower() if religion else 'life'}. Hoping to find a life companion who appreciates both the simple and adventurous moments.",
            f"Hey there! I'm {first_name}, a {gender.lower() if gender else 'person'} {profession.lower()} seeking a genuine connection. I have a keen interest in {interests.lower() if interests else 'various activities'} and cherish the principles of {religion.lower() if religion else 'life'}. Searching for a suitable partner who shares similar values and dreams.",
            f"Greetings! I'm {first_name}, a {gender.lower() if gender else 'person'} {marital_status.lower()} {profession.lower()} exploring the world of {interests.lower() if interests else 'various activities'}. I enjoy various activities and follow the principles of {religion.lower() if religion else 'life'}. Hoping to find a suitable life companion who appreciates both the simple and adventurous moments.",
            f"Hello! I'm {first_name}, a successful {gender.lower() if gender else 'person'} {profession.lower()} who is {marital_status.lower()}. My interests include {interests.lower() if interests else 'various activities'}, and I adhere to {religion.lower() if religion else 'life'} beliefs. Ready to embark on a new journey with a partner who values love, trust, and shared aspirations.",
            f"Hi there! I'm {first_name}, {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} with a passion for {interests.lower() if interests else 'various activities'}. When I'm not working, you'll find me engaged in various activities and embracing the teachings of {religion.lower() if religion else 'life'}. Hoping to meet someone special for a meaningful connection.",
            f"Hey! I'm {first_name}, balancing my {gender.lower() if gender else 'person'} {profession.lower()} duties with various activities and interests like {interests.lower() if interests else 'various activities'}. I find solace in following the path of {religion.lower() if religion else 'life'} in my daily life. Looking for a suitable life partner who values companionship, mutual respect, and shared values.",
            f"Hello, I'm {first_name}, {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} with a strong passion for {interests.lower() if interests else 'various activities'}. In my free time, I enjoy various activities and follow the principles of {religion.lower() if religion else 'life'}. Excited about the prospect of finding a suitable life partner who values love, laughter, and shared dreams.",
            f"Greetings! I'm {first_name}, actively pursuing {interests.lower() if interests else 'various activities'} with dedication. Beyond my professional life in {profession.lower() if profession else 'work'}, I find joy in various activities and hold firm to the beliefs of {religion.lower() if religion else 'life'}. Ready to explore the journey of life with a like-minded soulmate.",
            f"Hi, I'm {first_name}, excelling in the field of {profession.lower() if profession else 'work'} and embracing a {marital_status.lower()} life. Alongside my work, I enjoy various activities and have a keen interest in {interests.lower() if interests else 'various activities'}. Seeking a suitable life partner who values companionship, trust, and shared values.",
            f"Hey, I'm {first_name}, holding a profession in {profession.lower() if profession else 'work'} and embracing a {marital_status.lower()} status. During leisure hours, I engage in various activities and explore {interests.lower() if interests else 'various activities'}. Hoping to find a suitable life companion who shares similar values and dreams for the future.",
            f"Hello, I'm {first_name}, finding solace in various activities as a means of relaxation from my {profession.lower() if profession else 'work'} responsibilities. My interests span {interests.lower() if interests else 'various activities'}, and I adhere to the values of {religion.lower() if religion else 'life'}. Excited about the prospect of building a life filled with love, laughter, and shared moments.",
            f"Hi there! I'm {first_name}, professionally excelling as a {gender.lower() if gender else 'person'} {profession.lower()} with a deep passion for {interests.lower() if interests else 'various activities'}. In my leisure time, I find joy in various activities and follow the principles of {religion.lower() if religion else 'life'}. Eager to connect with a suitable life partner who values commitment and shared aspirations.",
            f"Hey, I'm {first_name}, actively pursuing my interests with dedication. Beyond the realms of {profession.lower() if profession else 'work'}, I derive joy from various activities. Firmly holding onto the beliefs of {religion.lower() if religion else 'life'}, I'm shaping my life with purpose. Excited about the possibility of finding a loving and compatible life partner.",
            f"Hello! I'm {first_name}, standing out in the {profession.lower() if profession else 'work'} domain and thriving in both professional and personal life. In addition to my career success, I enjoy various activities and have a keen interest in {interests.lower() if interests else 'various activities'}. Seeking a suitable life partner who values companionship, trust, and shared values.",
            f"Greetings! I'm {first_name}, thriving in the realm of {profession.lower() if profession else 'work'} and embracing a {marital_status.lower()} status. Outside of work, I indulge in various activities and explore {interests.lower() if interests else 'various activities'}. Excited about the prospect of building a strong connection with a like-minded life partner.",
            f"Hey there! I'm {first_name}, dedicating time to various activities for relaxation from my {profession.lower() if profession else 'work'} duties. With interests spanning {interests.lower() if interests else 'various activities'}, I follow the path of {religion.lower() if religion else 'life'} in my daily life, seeking harmony and fulfillment. Excited about connecting with a suitable life partner who values love, laughter, and shared dreams.",
            f"Hi, I'm {first_name}, excelling in the dynamic world of {profession.lower() if profession else 'work'} and fueled by an unwavering passion for {interests.lower() if interests else 'various activities'}. I gracefully balance the demands of my career with the joy found in various activities during tranquil moments. Guided by the timeless principles of {religion.lower() if religion else 'life'}, I'm ready to embark on a journey of love and companionship.",
            f"Greetings! I'm {first_name}, navigating life as {marital_status.lower()} with an insatiable appetite for exploration. Beyond the intricacies of {profession.lower() if profession else 'work'}, I immerse myself in the delight of various activities, threading a narrative interwoven with the rich fabric of {religion.lower() if religion else 'life'} beliefs. Excited about the prospect of sharing this journey with a like-minded life partner.",
            f"Hello, I'm {first_name}, standing as a paragon of success and thriving in the vibrant realm of {profession.lower() if profession else 'work'}. Beyond the professional accolades, I find solace in the nuanced artistry of various activities and cultivate a profound interest in {interests.lower() if interests else 'various activities'}. Guided by the compass of {religion.lower() if religion else 'life'} principles, I'm ready to illuminate the path with a life both accomplished and purposeful.",
            f"Hey, embark on the journey with me, {first_name}, a luminary in the field of {profession.lower() if profession else 'work'}. Beyond the corridors of expertise, I revel in the tapestry of various activities and explore the vast landscape of {interests.lower() if interests else 'various activities'}. Rooted in the profound teachings of {religion.lower() if religion else 'life'}, I'm eager to infuse each chapter of life with purpose and meaning.",
            f"Hi, I gracefully weave through the tapestry of life as {marital_status.lower()}, finding respite from the demands of {profession.lower() if profession else 'work'} in the sanctuary of various activities. With a heart captivated by {interests.lower() if interests else 'various activities'}, I follow the rhythm of {religion.lower() if religion else 'life'} principles, creating a harmonious symphony in my daily existence.",
            f"Hey! I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} seeking a suitable life companion. I enjoy various activities, especially {interests.lower() if interests else 'various activities'}, and value the principles of {religion.lower() if religion else 'life'}. Hoping to connect with someone who shares similar values and dreams for the future.",
            f"Hello there! I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} who finds joy in {interests.lower() if interests else 'various activities'}. When I'm not working, you'll catch me engaged in various activities and embracing the teachings of {religion.lower() if religion else 'life'}. Looking forward to meeting someone special for a meaningful relationship.",
            f"Hi, I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} with a passion for {interests.lower() if interests else 'various activities'}. Beyond work, you'll find me enjoying various activities and following the principles of {religion.lower() if religion else 'life'}. Excited about the prospect of building a loving and supportive connection.",
            f"Greetings! I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} who excels in {interests.lower() if interests else 'various activities'}. In my leisure time, I indulge in various activities and adhere to the values of {religion.lower() if religion else 'life'}. Hoping to find a suitable life partner who values love, trust, and shared aspirations.",
            f"Hi there! I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} dedicating time to various activities for relaxation from work. My interests span {interests.lower() if interests else 'various activities'}, and I follow the path of {religion.lower() if religion else 'life'}. Excited about connecting with someone who appreciates love, laughter, and shared dreams.",
            f"Hello, I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} with a strong passion for {interests.lower() if interests else 'various activities'}. Beyond my professional life, I find joy in various activities and follow the principles of {religion.lower() if religion else 'life'}. Eager to meet a suitable life partner who values companionship and shared values.",
            f"Hey, I'm {first_name}, actively pursuing my interests with dedication. Beyond my work in {profession.lower() if profession else 'work'}, I find joy in various activities and hold firm to the beliefs of {religion.lower() if religion else 'life'}. Excited about the prospect of building a strong connection with a like-minded life partner.",
            f"Hello there! I'm {first_name}, thriving in the realm of {profession.lower() if profession else 'work'} and embracing a {marital_status.lower()} status. Outside of work, I indulge in various activities and explore {interests.lower() if interests else 'various activities'}. Excited about the prospect of building a strong and loving connection.",
            f"Hey! I'm {first_name}, dedicating time to various activities for relaxation from my {profession.lower() if profession else 'work'} duties. With interests spanning {interests.lower() if interests else 'various activities'}, I follow the path of {religion.lower() if religion else 'life'} in my daily life, seeking harmony and fulfillment. Excited about connecting with someone who values love, laughter, and shared dreams.",
            f"Greetings! I'm {first_name}, navigating the dynamic world of {profession.lower() if profession else 'work'} with an unwavering passion for {interests.lower() if interests else 'various activities'}. I gracefully balance career demands with the joy found in various activities during tranquil moments. Guided by the timeless principles of {religion.lower() if religion else 'life'}, I'm ready to embark on a journey of love and companionship.",
            f"Hi, I'm {first_name}, a {marital_status.lower()} {gender.lower() if gender else 'person'} {profession.lower()} with an insatiable appetite for exploration. Beyond the intricacies of {profession.lower() if profession else 'work'}, I immerse myself in the delight of various activities, threading a narrative interwoven with the rich fabric of {religion.lower() if religion else 'life'} beliefs. Excited about the prospect of sharing this journey with a like-minded life partner.",
            f"Greetings! I'm {first_name}, standing tall as a paragon of success and thriving in both professional and personal life. In addition to my career success, I find solace in the nuanced artistry of various activities and cultivate a profound interest in {interests.lower() if interests else 'various activities'}. Guided by the compass of {religion.lower() if religion else 'life'} principles, I'm ready to illuminate the path with a life both accomplished and purposeful.",
            f"Hey, embark on the journey with me, {first_name}, a luminary in the field of {profession.lower() if profession else 'work'}. Beyond the corridors of expertise, I revel in the tapestry of various activities and explore the vast landscape of {interests.lower() if interests else 'various activities'}. Rooted in the profound teachings of {religion.lower() if religion else 'life'}, I'm eager to infuse each chapter of life with purpose and meaning.",
            f"Hi, I gracefully weave through the tapestry of life as {marital_status.lower()}, finding respite from the demands of {profession.lower() if profession else 'work'} in the sanctuary of various activities. With a heart captivated by {interests.lower() if interests else 'various activities'}, I follow the rhythm of {religion.lower() if religion else 'life'} principles, creating a harmonious symphony in my daily existence."

        ]

        random.shuffle(bio_templates)

        bios = []
        attempts = 0

        while len(bios) < 5:
            selected_bio = bio_templates[attempts % len(bio_templates)]

            if selected_bio not in generated_bios:
                generated_bios.add(selected_bio)
                bios.append(selected_bio)

            attempts += 1

            if len(generated_bios) >= MAX_BIOS:
                generated_bios.clear()

        response_data = [{"index": i+1, "bio": bio} for i, bio in enumerate(bios)]
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)