# MetaSync Solutions

## Overview

MetaSync Solutions provides a RESTful API for interacting with MetaTrader 5, enabling automated trading, market analysis, risk management, and strategy backtesting.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/metasync.git 
   cd metasync
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (create a `.env` file):

   ```plaintext
   MCP_URL=https://vincent.bespo.ai/api/v1/mcp/
   MCP_TRANSPORT=http
   ```

4. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

The API provides several endpoints for interacting with MetaTrader 5:

