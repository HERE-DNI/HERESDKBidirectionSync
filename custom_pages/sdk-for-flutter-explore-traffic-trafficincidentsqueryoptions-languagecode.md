---
title: "languageCode property"
slug: "sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-languagecode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- languageCode.html -->


<div>
<h1>languageCode property</h1></div>

<a href="/sdk-for-flutter-explore-core-languagecode">LanguageCode</a>?
        languageCode
<div class="features">getter/setter pair</div>


<p>The language code of the query.
It's the expected language of fields <a href="/sdk-for-flutter-explore-traffic-trafficincidentbase-description">TrafficIncidentBase.description</a> and <a href="/sdk-for-flutter-explore-traffic-trafficincident-summary">TrafficIncident.summary</a> in the relevant response.
However, the language code doesn't impact on <a href="/sdk-for-flutter-explore-traffic-trafficlocation-description">TrafficLocation.description</a>.
If the language code is null or not supported then response fields are expected in the original language of the country that the incident belongs to.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LanguageCode? languageCode;</code></pre>

 



</div>
`
}</HTMLBlock>
