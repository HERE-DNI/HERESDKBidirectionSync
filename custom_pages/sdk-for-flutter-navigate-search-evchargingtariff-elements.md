---
title: "elements property"
slug: "sdk-for-flutter-navigate-search-evchargingtariff-elements"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- elements.html -->


<div>
<h1>elements property</h1></div>

        
        List&lt;<a href="/sdk-for-flutter-navigate-search-evchargingtariffelement-class">EVChargingTariffElement</a>&gt;
elements
<div class="features">getter/setter pair</div>


<p>Elements composing the tariff. Each element can have multiple components. When multiple elements
are present, the associated condition helps the client to select the element that matches the
charging session. If no condition matches, the element without any condition applies.</p>
<p>Please note that tariff elements or conditions requiring access to vehicle APIs are not present in this API.
The provided elements can only be used to derive a price estimate, which in most cases is reasonably close to the final price.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;EVChargingTariffElement&gt; elements;</code></pre>

 



</div>
`
}</HTMLBlock>
