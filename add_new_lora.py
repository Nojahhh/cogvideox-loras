import datetime
import requests

def get_model_data_from_huggingface(link):
  repo_id = link.split('/')[-2] + '/' + link.split('/')[-1]
  api_url = f"https://huggingface.co/api/models/{repo_id}"
  response = requests.get(api_url)
  
  if response.status_code == 200:
    data = response.json()
    if 'author' not in data:
      data['author'] = input("Couldn't figure out the author of the lora. Please enter the author: ")
    if 'lastModified' not in data:
      data['lastModified'] = input("Couldn't figure out the last modified date of the lora. Please enter the last modified date: ")
    if 'createdAt' not in data:
      data['createdAt'] = input("Couldn't figure out the created date of the lora. Please enter the created date: ")
    if 'cardData' not in data:
      data['cardData'] = {'base_model': [input("Couldn't figure out the base model of the lora. Please enter the base model: ")]}
      data['cardData']['base_model'] = data['cardData']['base_model'].replace('https://huggingface.co/', '')
    elif 'base_model' not in data['cardData']:
      data['cardData']['base_model'] = [input("Couldn't figure out the base model of the lora. Please enter the base model: ")]
      data['cardData']['base_model'] = data['cardData']['base_model'].replace('https://huggingface.co/', '')
    return {
      'created_at': data.get('createdAt', 'Unknown').split('T')[0],
      'author': data.get('author', 'Unknown'),
      'last_modified': data.get('lastModified', 'Unknown').split('T')[0],
      'base_model': data.get('cardData', {}).get('base_model', ['Unknown'])[0]
    }
  else:
    print(f"Error: Unable to fetch data from Hugging Face API. Status code: {response.status_code}")
    return {
      'created_at': 'Unknown',
      'author': 'Unknown',
      'last_modified': 'Unknown',
      'base_model': 'Unknown'
    }

def add_lora_to_list(link, description, base_model, contributor, date_created, last_modified, date_added):
  entry = f"| [{link.split('/')[-2]+'/'+link.split('/')[-1]}]({link}) | {description} | [{base_model.split('/')[-2]+'/'+base_model.split('/')[-1]}]({'https://huggingface.co/'+base_model}) | {contributor} | {date_created} | {last_modified} | {date_added} |\n"
  
  with open("LORA_MODELS.md", "a") as file:
    file.write(entry)

def main():
  link = input("Enter the Hugging Face link of the LoRA model: ")
  
  while True:
    description = input("Enter the description of the LoRA model (max 250 characters): ")
    if len(description) <= 250:
      break
    print("Error: Description must be 250 characters or less. Please try again.")
  
  model_data = get_model_data_from_huggingface(link)
  base_model = model_data['base_model']
  contributor = model_data['author']
  last_modified = model_data['last_modified']
  date_created = model_data['created_at']
  date_added = datetime.date.today().strftime("%Y-%m-%d")

  add_lora_to_list(link, description, base_model, contributor, date_created, last_modified, date_added)

if __name__ == "__main__":
  main()