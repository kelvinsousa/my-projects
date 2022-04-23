from pytube import YouTube


link = str(input('Insira o link para download: ')).strip()
yt = YouTube(link)
print(f'Baixando...{yt.title}')
yt = yt.streams.get_highest_resolution()
caminho = 'MacintoshSSD/Users/user/Documents'
yt.download(output_path=caminho)