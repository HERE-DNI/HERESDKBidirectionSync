---
title: "IsolineOptions.withTruckOptions constructor"
slug: "sdk-for-flutter-navigate-routing-isolineoptions-isolineoptions-withtruckoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptions.withTruckOptions.html -->


<div>
<h1>IsolineOptions.withTruckOptions constructor</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the constructor with RoutingOptions parameter instead.")</li>
</ol>
</div>
IsolineOptions.withTruckOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a> calculationOptions, </li>
<li><a class="deprecated" href="sdk-for-flutter-navigate-routing-truckoptions-class">TruckOptions</a> truckOptions</li>
</ol>)
    

<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and truck routing options.</p>
<ul>
<li>
<p><code>calculationOptions</code> The options to be used to calculate this isoline.</p>
</li>
<li>
<p><code>truckOptions</code> The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the constructor with RoutingOptions parameter instead.")

factory IsolineOptions.withTruckOptions(IsolineOptionsCalculation calculationOptions, TruckOptions truckOptions) =&gt; $prototype.withTruckOptions(calculationOptions, truckOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
