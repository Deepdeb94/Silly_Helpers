def main():
    
    place = input('Name to know their address: ')

    match place:
        case 'Aaron' | 'Niki' | 'Pulovi':
            print('Thilixu')
        case 'Hukhevi':
            print('Xukiye')
        case 'Onito' | 'Mughavi' | 'Anguvi':
            print('Super Market')
        case _:
            print('Who')

main()