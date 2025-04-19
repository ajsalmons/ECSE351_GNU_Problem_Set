# ECSE 351 GNU Problem Set
<br>Alden Salmons
<br>April 18th, 2025

# Problem: Baba Yaga's Hut Simulation
- User can vary amplitude, frequency, phase, and offset of two signals
- See time domain and phasor views

# Approach
- UI designed for 19 x 10 aspect ratio (1080p minus taskbar and menu bar)
    - Maximize area of Time Series and XY Plot in UI
    - Keep XY Plot as square as possible
- Signal source control
    - Use QT GUI Dial blocks
    - Separate controls for each parameter and signal (Y1 and Y2)
    - Ranges and steps
        - Amplitude: 0 to 1, step of 0.01, default 1
        - Frequency: 0 to 5 Hz, step of 0.1 Hz, default 0.5 Hz
        - (Initial) Phase: 0 to 360 degress, step of 5 degress, default 90 degrees between Y1 and Y2
        - Offset: -1 to 1, step of 0.02, default 0
- Signal Generation
    - Generate a complex sinusoid from a Signal Source block
    - Apply Frequency and Phase Shift blocks in two parallel streams/signals
    - Convert Complex to Float
    - Apply Multiply Const (Amplitude) and Add Const (DC offset) blocks
    - Multiply the two signals to get Y1 x Y2
- Time Series
    - QT GUI Time Sink block
    - 4s Window
- XY Plot
    - Converted Signal 1 and Signal 2 from float to one complex stream
    - Used Constellation Sink block, displays 10s of data (Maximum period of either signal)

# Difficulties
- Phase difference drifts slightly over simulation time
    - Does global sampling rate have anything to do with this?
- Phase accumulation from changing and reverting frequency
    - Need to zero phase manually
    - Makes it difficult to set absolute phase difference
    - Will have to add note to instructions
- Changing the Delay on the Time Sink Control Panel can cause the UI to crash
    - Will keep controls for now because very useful
- Changing x scale of Time Sink can cause simulation to freeze
    - Makes it difficult to see effects of AM
- Can't update Time Sink parameters live (Other than Control Panel)

# File Versions
- phase_lab_v1.grc
    - Initial attempt, generated two signals in separate signal blocks
    - Noticed phase issues, tried to resolve with attempt 2
- phase_lab_v2.grc - *Final version*
    - Changed to two complex signal sources, applied frequency and phase shift blocks
    - Added back in the Constellation Sink for the XY Plot
    - Didn't fix the phase issues as I had hoped, but sticking with this version

# References
1. GNU Radio Wiki https://wiki.gnuradio.org/index.php/Main_Page
2. Chat GPT (https://chatgpt.com/)
    1. Advice on color selection
    2. Troubleshooting stream to vector
    3. Advice to use constellation block for XY plot
