
import streamlit as st


def footer_home():
    st.markdown("""
        <div style="
            margin-top: 40px;
            padding: 12px;
            text-align: center;
            color: #E0E3FF;
            font-size: 13px;
            line-height: 1.8;
        ">
            <div style="font-size: 20px; font-weight: 800;">
                AttendIQ
            </div>
            <div>
                Smarter Attendance. Powered by AI.
            </div>
            <div style="font-size: 11px; opacity: 0.8;">
                © 2026 AttendIQ
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top: 28px;
            padding: 10px;
            text-align: center;
            color: #5865F2;
            font-size: 12px;
        ">
            AttendIQ
            <span style="color: #687493;">
                | Smart Attendance System
            </span>
        </div>
    """, unsafe_allow_html=True)
