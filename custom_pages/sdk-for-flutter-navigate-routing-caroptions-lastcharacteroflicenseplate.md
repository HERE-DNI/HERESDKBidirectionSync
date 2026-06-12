---
title: "lastCharacterOfLicensePlate property"
slug: "sdk-for-flutter-navigate-routing-caroptions-lastcharacteroflicenseplate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lastCharacterOfLicensePlate.html -->


<div>
<h1>lastCharacterOfLicensePlate property</h1></div>

        
        String?
        lastCharacterOfLicensePlate
<div class="features">getter/setter pair</div>


<p>Specifies the last character of a vehicle's license plate, typically used to
evaluate traffic restrictions in certain environmental or low-emission zones.
In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may
be restricted on certain days or in certain areas to reduce congestion and emissions.
When this value is provided, the HERE SDK considers it during route calculation to
avoid roads or areas where your vehicle may be restricted based on local regulations.
Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".</p>
<p>If this value is not set, such license plate-based restrictions are ignored, and
routing is performed without considering them.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? lastCharacterOfLicensePlate;</code></pre>

 



</div>
`
}</HTMLBlock>
