import { Html, Head, Main, NextScript } from "next/document";

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <title>Destiny Care Home - Compassionate Caregivers</title>

        {/* SEO Meta Tags */}
        <meta
          name="description"
          content="Destiny Care Home provides compassionate and professional care services for seniors, ensuring a safe and nurturing environment for your loved ones."
        />
        <meta
          name="keywords"
          content="Destiny Care Home, senior care, elderly care, assisted living, memory care, nursing home, compassionate care, senior living"
        />
        <meta name="author" content="Destiny Care Home" />

        {/* Open Graph Meta Tags for SMO */}
        <meta
          property="og:title"
          content="Destiny Care Home - Compassionate Caregivers"
        />
        <meta
          property="og:description"
          content="At Destiny Care Home, we provide professional and compassionate care services for seniors, ensuring a safe and nurturing environment."
        />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://www.destinycarehome.com" />
        <meta
          property="og:image"
          content="https://www.destinycarehome.com/destiny-logo.png"
        />
        <meta property="og:site_name" content="Destiny Care Home" />

        {/* Twitter Card Meta Tags */}
        <meta name="twitter:card" content="summary_large_image" />
        <meta
          name="twitter:title"
          content="Destiny Care Home - Compassionate Caregivers"
        />
        <meta
          name="twitter:description"
          content="Destiny Care Home offers professional and compassionate care services for seniors, ensuring a safe and nurturing environment."
        />
        <meta
          name="twitter:image"
          content="https://www.destinycarehome.com/destiny-logo.png"
        />
        <meta name="twitter:site" content="@DestinyCareHome" />

        {/* Existing links and scripts */}
        <link
          href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700"
          rel="stylesheet"
        />
        <script
          async
          src="https://kit.fontawesome.com/42d5adcbca.js"
          crossOrigin="anonymous"
        ></script>
        <link href="/css/nucleo-icons.css" rel="stylesheet" />
        <link href="/css/nucleo-svg.css" rel="stylesheet" />
        <link
          href="/css/soft-ui-dashboard-tailwind.css?v=1.0.5"
          rel="stylesheet"
        />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}