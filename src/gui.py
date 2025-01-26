import PySimpleGUI as sg
import os

class CrisisCoreGUI:
    def __init__(self):
        sg.theme('DarkBlue')
        self.window = self._create_window()
        
    def _create_window(self):
        layout = [
            [sg.Text('CrisisCore-Systems Enterprise Suite', font=('Helvetica', 20), justification='center')],
            [sg.HSep()],
            [sg.Text('Input File:', size=(12, 1)), 
             sg.Input(key='-FILE-', size=(40, 1)),
             sg.FileBrowse(file_types=(('Text Files', '*.txt'), ('All Files', '*.*')))],
            [sg.Text('Chunk Size (KB):', size=(12, 1)),
             sg.Input('1024', key='-SIZE-', size=(10, 1))],
            [sg.HSep()],
            [sg.Text('Processing Status:', size=(12, 1))],
            [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
            [sg.Multiline(size=(60, 10), key='-OUTPUT-', reroute_stdout=True)],
            [sg.Button('Process', size=(10, 1)),
             sg.Button('Clear', size=(10, 1)),
             sg.Button('Exit', size=(10, 1))]
        ]
        
        return sg.Window('CrisisCore-Systems Enterprise v1.0',
                        layout,
                        finalize=True,
                        size=(800, 600))
                        
    def run(self):
        while True:
            event, values = self.window.read()
            
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
                
            if event == 'Process':
                try:
                    input_file = values['-FILE-']
                    chunk_size = int(values['-SIZE-']) * 1024
                    
                    if not os.path.exists(input_file):
                        sg.popup_error('Error: Input file not found')
                        continue
                        
                    splitter = CrisisCoreSplitter(input_file, chunk_size)
                    self.window['-PROGRESS-'].update(50)
                    splitter.split_file()
                    self.window['-PROGRESS-'].update(100)
                    
                except Exception as e:
                    sg.popup_error(f'Error: {str(e)}')
                    self.window['-PROGRESS-'].update(0)
                    
            if event == 'Clear':
                self.window['-OUTPUT-'].update('')
                self.window['-PROGRESS-'].update(0)
                
        self.window.close()

if __name__ == '__main__':
    gui = CrisisCoreGUI()
    gui.run()
