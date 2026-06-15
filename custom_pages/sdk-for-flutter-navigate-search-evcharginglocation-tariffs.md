---
title: "tariffs property"
slug: "sdk-for-flutter-navigate-search-evcharginglocation-tariffs"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- tariffs.html -->


<div>
<h1>tariffs property</h1></div>
<section id="getter">

List&lt;<a href="sdk-for-flutter-navigate-search-evchargingtariff-class">EVChargingTariff</a>&gt;
tariffs


<p>List of tariffs or price plans for the connectors of the charging station.
Tariffs are typically connector-type specific. Hence, they are always linked with connectors
and/or connector groups, by indexes to this list.</p>
<p>This property is set only when data is available and when <code>EVSearchOptions.additional_features</code>
include either <code>EVChargingLocationFeature.EVSES</code> or <code>EVChargingLocationFeature.CONNECTOR_GROUPS</code>.</p>
<p>By default, the list includes tariffs for ad-hoc charging, per connector type,
for EVSEs that accept payment without registering.
Gets the list of tariffs or price plans for the connectors of the charging station.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;EVChargingTariff&gt; get tariffs;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
