�
    I�Ag�  �                   �  � d dl Z d dlmZ d dlmZ d dlZd dlZd dlZd dlZd dl	Z	d� Z
d� Zd� Zd� Zedk(  �r# e�         e
�        	  ed	�      Z ej                  d
�      Z eee�      rn�% ed�      Z ed�      Z ed�      Z e ed�      �      Z	  ed�      j/                  �       Zedv rn	 ed�       �$dZedk(  r ed�      ZdZ ed�      j/                  �       Zedk(  rW ed�       g Z	  e�       Zej?                  �       jA                  �       dk(  rnejC                  e�       �;djE                  e�      Z ed�        eeeeeeeeee�	        ed�       yy)�    N)�MIMEText)�MIMEMultipartc                  �D  � t        j                  t         j                  dk(  rdnd�       d} t        | �       t        d�       t        | �       t        dt	        j
                  �       j                  �       � d��       t        d�       t        d	�       t        | d
z   �       y )N�posix�clear�clsu  🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥uV   💀                        WELCOME TO THE SPAM APOCALYPSE                        💀u   🌌 Script Author: z aka superXuseru*   🔒 github: https://github.com/SuperXuseruB   ⚠️  Disclaimer: If you get caught, you never got this from me.�
)�os�system�name�print�platform�node�upper)�borders    �x.py�display_authorr      sw   � ��I�I����G�+�g��7��F�	�&�M�	�
R�S�	�&�M�	� �����!6�!6�!8� 9��
I�J�	�
6�7�	�
N�O�	�&�4�-��    c                 �J  � t        d�       	 t        j                  dd�      }|j                  �        |j	                  | |�       |j                  �        t        d�       y# t        j                  $ r t        d�       Y yt        $ r}t        d|� d	��       Y d }~yd }~ww xY w)
Nu5   
🔒 VALIDATING YOUR ACCESS TO THE SPAM ARSENAL 🔒�smtp.gmail.com�K  u0   ✅ AUTHENTICATION SUCCESSFUL. YOU’RE IN. ✅
TuC   ❌ ACCESS DENIED: INVALID GMAIL OR PASSWORD, HACKER WANNA-BE. ❌
Fu   ❌ ERROR: u    ❌
)r   �smtplib�SMTP�starttls�login�quit�SMTPAuthenticationError�	Exception)�email�password�server�es       r   �validate_credentialsr#      s�   � �	�
B�C�����.��4���������U�H�%������A�B����*�*� ��T�U��� ���A�3�f�%�&����s   �AA! �!B"�B"�	B�B"c	           
      �  � t        d�       	 t        j                  dd�      }	|	j                  �        |	j	                  | |�       t        d�       g d�}
t        |�      D ]�  }t        d�      }|� d| � d�|d	<   ||d
<   |dk(  rt        j                  |
�      |d<   n
|dk(  r||d<   t        |d�      }|j                  |�       |j                  �       rt        |d�      }|j                  |�       |	j                  | ||j                  �       �       t        d|dz   � d|� d|d   � ��       t        j                  t        j                   dd�      �       �� t        d�       	j%                  �        t        d�       y # t"        $ r}t        d|� d��       Y d }~�9d }~ww xY w# 	j%                  �        t        d�       w xY w)Nu"   
💣 LOADING THE SPAM NUKES 💣
r   r   u.   🚀 CONNECTED. DEPLOYING THE PAYLOAD... 🚀
)u#   🔥 YOUR ACCOUNT IS IN DANGER 🔥u%   💸 YOU’VE WON BIG! CLICK NOW 💸u(   ⚠️ URGENT: VERIFY IMMEDIATELY ⚠️u    🌟 EXCLUSIVE OFFER INSIDE 🌟u    💀 SPAM MASTER HAS STRUCK 💀u'   🔥🔥 TOTAL CHAOS INITIATED 🔥🔥�alternativez <�>�From�To�	automatic�Subject�custom�plain�htmlu   💥 [�   �/z] SPAM SENT: g      �?g      �?u/   
🎉 PAYLOAD DELIVERED. CHAOS UNLEASHED. 🎉
u   💔 ERROR: u    💔
u/   🛑 MISSION COMPLETE. RETURNING TO BASE. 🛑
)r   r   r   r   r   �ranger   �random�choicer   �attach�strip�sendmail�	as_string�time�sleep�uniformr   r   )r   r    �target_email�message�count�spoofed_name�subject_choice�custom_subject�	html_coder!   �subject_lines�i�msg�
plain_part�	html_partr"   s                   r   �	send_spamrF   *   s�  � �	�
0�1�*B����.��4���������U�H�%��?�@�
�� �u��A���.�C�)�N�"�U�G�1�5�C��K�$�C��I� ��,�!'���}�!=��I���8�+�!/��I�� "�'�7�3�J��J�J�z�"���� �$�Y��7�	��
�
�9�%��O�O�E�<�����A��F�1�q�5�'��5�'��s�9�~�6F�G�H��J�J�v�~�~�c�3�/�0�) �, 	�A�B� 	�����@�A��	 � )���Q�C�w�'�(�(��)�� 	�����@�A�s*   �EE< �<	F�F�F! �F�F! �!F>c                  �   � d} t        | �       t        d�       t        | �       t        d�       t        dt        j                  �       � dt        j                  �       � ��       t        dt        j                  �       � ��       t        d�       y )Nu�   ✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨u?   🌌 SCRIPT OF LEGENDS | BUILT FOR THE ELITE BY SUPERXUSER 🌌z
SYSTEM INFO:u   🖥️  OS: � u   ⚙️  Machine: u)   📡 READY TO LAUNCH THE SPAM APOCALYPSE
)r   r   r   �releaser   )�starss    r   �bannerrK   X   sn   � ��E�	�%�L�	�
K�L�	�%�L�	�
��	�M�(�/�/�+�,�A�h�.>�.>�.@�-A�
B�C�	��h�m�m�o�.�
/�0�	�
6�7r   �__main__u   📧 Enter your Gmail: u    🔑 Enter your Gmail password: u   🎯 Enter the target Gmail: u'   🕵️ Enter the spoofed sender name: u'   ✉️ Enter the spam message to send: u)   🔢 Enter how many spam emails to send: uB   📋 Do you want [automatic] random subjects or [custom] subject? )r)   r+   u5   ⚠️ Invalid choice! Enter 'automatic' or 'custom'.� r+   u    🎯 Enter your custom subject: u1   📄 Do you want to include HTML content? [y/n]: �yuF   ✍️ Enter your HTML code below. Type 'END' on a new line to finish:�ENDr	   u+   
💀 INITIATING SPAM ATTACK SEQUENCE 💀
u6   🔥 OPERATION COMPLETE. WREAK HAVOC RESPONSIBLY. 🔥)#r   �email.mime.textr   �email.mime.multipartr   r1   r7   �getpassr
   r   r   r#   rF   rK   �__name__�input�sender_email�sender_passwordr:   r=   �spam_message�int�
spam_count�lowerr>   r   r?   r@   �html_option�
html_lines�liner4   r   �append�join� r   r   �<module>ra      s�  �� � $� .� � � � 	� �	�� ,B�\8� �z��
�H���
��6�7��)�'�/�/�*L�M����o�>��	 � �8�9�L��B�C�L��B�C�L��U�F�G�H�J� ��c�d�j�j�l���4�4���E�F�	 � �N���!��A�B�� �I��K�L�R�R�T�K��c���V�W��
���7�D��z�z�|�!�!�#�u�,�����d�#�	 �
 �I�I�j�)�	�	�
9�:��l�O�\�<��Ua�cq�  tB�  DM�  N�	�
B�C�S r   