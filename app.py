import gradio as gr

from app_playai import demo as demo_playai
from app_allenai import demo as demo_allenai
from app_claude import demo as demo_claude
from app_experimental import demo as demo_experimental
from app_fireworks import demo as demo_fireworks
from app_flux import demo as demo_flux
from app_gemini import demo as demo_gemini
from app_groq import demo as demo_groq
from app_hyperbolic import demo as demo_hyperbolic
from app_ltx_video import demo as demo_ltx_video
from app_marco_o1 import demo as demo_marco_o1
from app_mistral import demo as demo_mistral
from app_nvidia import demo as demo_nvidia
from app_openai import demo as demo_openai
from app_perplexity import demo as demo_perplexity
from app_qwen import demo as demo_qwen
from app_sambanova import demo as demo_sambanova
from app_together import demo as demo_together
from app_xai import demo as demo_grok

# Advanced theme configuration with enhanced animations
css = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(1deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes glow {
    0% { text-shadow: 0 0 10px rgba(255,255,255,0.8), 0 0 20px rgba(255,255,255,0.8), 0 0 30px rgba(255,255,255,0.8); }
    50% { text-shadow: 0 0 20px rgba(255,255,255,0.8), 0 0 30px rgba(255,255,255,0.8), 0 0 40px rgba(255,255,255,0.8); }
    100% { text-shadow: 0 0 10px rgba(255,255,255,0.8), 0 0 20px rgba(255,255,255,0.8), 0 0 30px rgba(255,255,255,0.8); }
}

@keyframes fadeInBlur {
    from { 
        opacity: 0;
        transform: translateY(20px) scale(0.98);
        filter: blur(10px);
    }
    to { 
        opacity: 1;
        transform: translateY(0) scale(1);
        filter: blur(0);
    }
}

@keyframes cyber-glow {
    0% { box-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 15px #0ff; }
    50% { box-shadow: 0 0 10px #f0f, 0 0 20px #f0f, 0 0 30px #f0f; }
    100% { box-shadow: 0 0 5px #0ff, 0 0 10px #0ff, 0 0 15px #0ff; }
}

:root {
    --background-fill-primary: #0a0b1e;
    --border-color-primary: #2a2b4a;
    --neon-blue: #0ff;
    --neon-purple: #f0f;
    --space-black: #0a0b1e;
}

* {
    font-family: 'Space Grotesk', sans-serif;
}

body {
    background: radial-gradient(circle at center, #1a1b3e 0%, #0a0b1e 100%);
    color: #fff;
}

#custom-header {
    background: linear-gradient(135deg, rgba(42, 43, 74, 0.7), rgba(10, 11, 30, 0.7));
    backdrop-filter: blur(20px);
    padding: 2.5rem;
    border-radius: 20px;
    margin: 1.5rem;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.1);
    border: 1px solid rgba(0, 255, 255, 0.1);
    position: relative;
    overflow: hidden;
}

#custom-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, 
        rgba(0, 255, 255, 0.1) 0%,
        transparent 50%);
    animation: gradient 15s linear infinite;
}

#custom-header h1 {
    color: white;
    font-size: 3.5rem;
    margin: 0;
    text-align: center;
    font-weight: 700;
    letter-spacing: 2px;
    animation: float 6s ease-in-out infinite, glow 3s ease-in-out infinite;
    position: relative;
    z-index: 1;
}

#custom-header p {
    color: var(--neon-blue);
    text-align: center;
    margin: 1rem 0 0 0;
    font-size: 1.3rem;
    opacity: 0.9;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.tab-nav {
    background: rgba(42, 43, 74, 0.7) !important;
    backdrop-filter: blur(20px) !important;
    border-radius: 15px !important;
    padding: 1rem !important;
    margin: 1rem !important;
    border: 1px solid rgba(0, 255, 255, 0.1) !important;
    animation: cyber-glow 4s infinite alternate !important;
}

.tab-nav button {
    color: white !important;
    border-radius: 10px !important;
    margin: 0.4rem !important;
    padding: 1rem 1.5rem !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    background: rgba(10, 11, 30, 0.7) !important;
    border: 1px solid rgba(0, 255, 255, 0.2) !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    font-weight: 500 !important;
}

.tab-nav button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    background: rgba(0, 255, 255, 0.1) !important;
    border-color: var(--neon-blue) !important;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.3) !important;
}

.tab-nav button.selected {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.2), rgba(255, 0, 255, 0.2)) !important;
    border: 1px solid var(--neon-blue) !important;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.4) !important;
}

.message {
    border-radius: 15px !important;
    padding: 1.5rem !important;
    margin: 1rem 0 !important;
    background: rgba(42, 43, 74, 0.3) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(0, 255, 255, 0.1) !important;
    animation: fadeInBlur 0.5s ease-out !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.message:hover {
    transform: translateY(-3px) scale(1.01) !important;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.2) !important;
}

.user-message {
    background: linear-gradient(135deg, rgba(0, 255, 255, 0.1), rgba(42, 43, 74, 0.3)) !important;
    border-left: 4px solid var(--neon-blue) !important;
}

.bot-message {
    background: linear-gradient(135deg, rgba(255, 0, 255, 0.1), rgba(42, 43, 74, 0.3)) !important;
    border-left: 4px solid var(--neon-purple) !important;
}

textarea, input[type="text"] {
    background: rgba(10, 11, 30, 0.7) !important;
    border: 1px solid rgba(0, 255, 255, 0.2) !important;
    border-radius: 12px !important;
    color: white !important;
    backdrop-filter: blur(10px) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: var(--neon-blue) !important;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.2) !important;
    transform: translateY(-2px) !important;
}

::-webkit-scrollbar {
    width: 12px;
    height: 12px;
    background: var(--space-black);
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
    border-radius: 6px;
    border: 3px solid var(--space-black);
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, var(--neon-purple), var(--neon-blue));
}

.loading-container {
    position: relative;
    width: 50px;
    height: 50px;
}

@keyframes neural-pulse {
    0% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.5); opacity: 0; }
    100% { transform: scale(1); opacity: 0.5; }
}

.neural-node {
    position: absolute;
    width: 4px;
    height: 4px;
    background: var(--neon-blue);
    border-radius: 50%;
    animation: neural-pulse 2s infinite;
}
"""

with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    with gr.Column():
        gr.HTML("""
            <div id="custom-header">
                <h1>🤖 NeuraTalk AI</h1>
                <p>Advanced Neural Interface for Multi-Model AI Communication</p>
                <style>
                    @keyframes neural-spark {
                        0% { transform: scale(0) rotate(0deg); opacity: 0; }
                        50% { transform: scale(1) rotate(180deg); opacity: 1; }
                        100% { transform: scale(0) rotate(360deg); opacity: 0; }
                    }
                    .neural-spark {
                        position: absolute;
                        width: 2px;
                        height: 2px;
                        background: linear-gradient(135deg, var(--neon-blue), var(--neon-purple));
                        border-radius: 50%;
                        animation: neural-spark 3s infinite;
                    }
                </style>
                <script>
                    function createNeuralNetwork() {
                        const header = document.getElementById('custom-header');
                        const particleCount = 30;
                        const connectionCount = 20;
                        
                        // Create particles
                        for (let i = 0; i < particleCount; i++) {
                            const spark = document.createElement('div');
                            spark.className = 'neural-spark';
                            spark.style.left = Math.random() * 100 + '%';
                            spark.style.top = Math.random() * 100 + '%';
                            spark.style.animationDelay = Math.random() * 3 + 's';
                            header.appendChild(spark);
                        }
                        
                        // Create neural connections
                        const canvas = document.createElement('canvas');
                        canvas.style.position = 'absolute';
                        canvas.style.top = '0';
                        canvas.style.left = '0';
                        canvas.style.width = '100%';
                        canvas.style.height = '100%';
                        canvas.style.pointerEvents = 'none';
                        header.appendChild(canvas);
                        
                        const ctx = canvas.getContext('2d');
                        
                        function animate() {
                            canvas.width = header.offsetWidth;
                            canvas.height = header.offsetHeight;
                            
                            ctx.strokeStyle = 'rgba(0, 255, 255, 0.1)';
                            ctx.lineWidth = 1;
                            
                            for (let i = 0; i < connectionCount; i++) {
                                const x1 = Math.random() * canvas.width;
                                const y1 = Math.random() * canvas.height;
                                const x2 = Math.random() * canvas.width;
                                const y2 = Math.random() * canvas.height;
                                
                                ctx.beginPath();
                                ctx.moveTo(x1, y1);
                                ctx.lineTo(x2, y2);
                                ctx.stroke();
                            }
                            
                            requestAnimationFrame(animate);
                        }
                        
                        animate();
                    }
                    
                    window.addEventListener('load', createNeuralNetwork);
                </script>
            </div>
        """)
        
        with gr.Tabs(elem_classes="tab-nav"):
            with gr.Tab("PlayAI"):
                demo_playai.render()
            with gr.Tab("Grok"):
                demo_grok.render()
            with gr.Tab("Hyperbolic"):
                demo_hyperbolic.render()
                gr.Markdown(
                    """
                <div>
                    <img src="https://storage.googleapis.com/public-arena-asset/hyperbolic_logo.png" alt="Hyperbolic Logo" style="height: 50px; margin-right: 10px;">
                </div>

                **Note:** This model is supported by Hyperbolic. Build your AI apps at [Hyperbolic](https://app.hyperbolic.xyz/).
                """
                )
            with gr.Tab("Gemini"):
                demo_gemini.render()
            with gr.Tab("ChatGPT"):
                demo_openai.render()
            with gr.Tab("Claude"):
                demo_claude.render()
            with gr.Tab("Qwen"):
                demo_qwen.render()
            with gr.Tab("Allen AI"):
                demo_allenai.render()
            with gr.Tab("Perplexity"):
                demo_perplexity.render()
            with gr.Tab("Experimental"):
                demo_experimental.render()
            with gr.Tab("Meta Llama"):
                demo_sambanova.render()
                gr.Markdown(
                    "**Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/)."
                )
            with gr.Tab("Marco-o1"):
                demo_marco_o1.render()
            with gr.Tab("LTX Video"):
                demo_ltx_video.render()
            with gr.Tab("Groq"):
                demo_groq.render()
            with gr.Tab("Mistral"):
                demo_mistral.render()
            with gr.Tab("Fireworks"):
                demo_fireworks.render()
            with gr.Tab("Together"):
                demo_together.render()
            with gr.Tab("NVIDIA"):
                demo_nvidia.render()
            with gr.Tab("Flux"):
                demo_flux.render()

if __name__ == "__main__":
    demo.queue(api_open=False).launch(ssr_mode=False, show_api=False)
