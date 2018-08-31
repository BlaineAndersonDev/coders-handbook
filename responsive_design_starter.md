# Responsive Design Experiment Examples:
### Copy & Paste Options:

#### Blank Copy & Pastes:
  * A __Blank__ *Flex* & *Media Query* block:
  ```
    .blank_flex_media{
      display: flex;
      flex-flow: column wrap;
      justify-content: center;
      align-items: center;
      text-align: center;
      color: white;
      background: #323232;
      // Most Smartphones Mobiles (Portrait)
        @media (min-width: 320px) and (max-width: 480px) {
        }
      // Low Resolution Tablets, Mobiles (Landscape)
        @media (min-width: 481px) and (max-width: 767px) {
        }
      // Tablets, Ipads (portrait)
        @media (min-width: 768px) and (max-width: 1024px) {
        }
      // Laptops, Desktops
        @media (min-width: 1025px) and (max-width: 1280px) {
        }
      // Desktops
        @media (min-width: 1281px) {
        }
    }
  ```
#### Starter - Flexbox & Media Query Copy & Pastes:
  * A __Wrapper__ for the entire page:
  ```
    #wrapper_starter{
      color: white;
      background: #323232;
      display: flex;
      flex-flow: column wrap;
      justify-content: center;
      align-items: center;
      text-align: center;
    }
  ```
  * A __Container__ for flexible items:
  ```
    .container_starter{
      width: 80%;
      height: 80%;
      display: flex;
      flex-flow: row wrap;
      justify-content: center;
      align-items: center;
      border-bottom: 3px white solid;
      // Most Smartphones Mobiles (Portrait)
        @media (min-width: 320px) and (max-width: 480px) {
          padding: 5px;
        }
      // Low Resolution Tablets, Mobiles (Landscape)
        @media (min-width: 481px) and (max-width: 767px) {
          padding: 8px;
        }
      // Tablets, Ipads (portrait)
        @media (min-width: 768px) and (max-width: 1024px) {
          padding: 12px;
        }
      // Laptops, Desktops
        @media (min-width: 1025px) and (max-width: 1280px) {
          padding: 16px;
        }
      // Desktops
        @media (min-width: 1281px) {
          padding: 20px;
        }
    }
  ```
  * An __Item__ maintaining a certain size:
  ```
    .item_starter{
      // Most Smartphones Mobiles (Portrait)
        @media (min-width: 320px) and (max-width: 480px) {
          border: 1px red solid;
          flex: 1 0 calc(100% * (1/3) - 30px);
          margin: 5px;
          padding: 5px;
          font-size: 0.8em;
        }
      // Low Resolution Tablets, Mobiles (Landscape)
        @media (min-width: 481px) and (max-width: 767px) {
          border: 1px blue solid;
          flex: 1 0 calc(100% * (1/4) - 40px);
          margin: 5px;
          padding: 5px;
          font-size: 0.8em;
        }
      // Tablets, Ipads (portrait)
        @media (min-width: 768px) and (max-width: 1024px) {
          border: 1px yellow solid;
          flex: 1 0 calc(100% * (1/5) - 60px);
          margin: 7px;
          padding: 10px;
          font-size: 1em;
        }
      // Laptops, Desktops
        @media (min-width: 1025px) and (max-width: 1280px) {
          border: 1px purple solid;
          flex: 1 0 calc(100% * (1/3) - 80px);
          margin: 7px;
          padding: 10px;
          font-size: 2em;
        }
      // Desktops
        @media (min-width: 1281px) {
          border: 1px orange solid;
          flex: 1 0 calc(100% * (1/5) - 80px);
          margin: 10px;
          padding: 12px;
          font-size: 2.5em;
        }
    }
  ```
