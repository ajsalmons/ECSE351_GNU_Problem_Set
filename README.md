ECSE351 GNU Problem Set
<br>Alden Salmons
<br>April 18th, 2025

# Problem: Baba Yaga's Hut Simulation
- User can vary amplitude, frequency, and phase
- See time domain and phasor views

Create a block diagram with a GUI that simulates the Phase Lab. In the GUI, the user should be able
to vary the amplitude, frequency and phase of a signal, and see the time domain and phasor view in real
time. (Consider the QT GUI Vector Sink block.) An excellent version will be used in future curriculum,
with acknowledgment of your work.

# Approach
- UI designed for 1920 x 1080p display (minus taskbar), should also scale well for similar aspect ratios
    - Maximize area of Time Series and XY Plot in UI
- Amplitude, frequency, and phase control
    - Use QT GUI Dial blocks
    - Separate controls for each parameter and signal (Y1 and Y2)
    - Ranges and steps
        - Amplitude: 0 to 1, step of 0.01, default 1
        - Frequency: 0 to 5 Hz, step of 0.1 Hz, default
- Signal Generation
    - Generate sine waves from two Signal Source blocks
    - Parameters controlled by Dials
- Time Series
    - QT GUI Time Sink block
    - 4s Window
-     

# Difficulties
- Phase difference drifts slightly over simulation time
    - Does global sampling rate have anything to do with this?
    - Solution: Will have to combine both signal sources (so the two signals are phase-locked)
- Changing the Delay on the Time Sink Control Panel can cause the UI to crash
    - Will keep controls for now because very useful
- Can't update Time Sink parameters live (Other than Control Panel)
- 

# References
1. GNU Radio Wiki https://wiki.gnuradio.org/index.php/Main_Page
2. Chat GPT (https://chatgpt.com/)
    1. Advice on color selection
    2. Troubleshooting stream to vector block
    3. Advice to use constellation block for XY plot
