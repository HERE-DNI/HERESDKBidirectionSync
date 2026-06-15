---
title: "IsolineOptions.withRoutingOptions constructor"
slug: "sdk-for-flutter-explore-routing-isolineoptions-isolineoptions-withroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IsolineOptions.withRoutingOptions.html -->


<div>
<h1>IsolineOptions.withRoutingOptions constructor</h1></div>

IsolineOptions.withRoutingOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-routing-isolineoptionscalculation-class">IsolineOptionsCalculation</a> calculationOptions, </li>
<li><a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a> routingOptions</li>
</ol>)
    

<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and routing options.</p>
<p><strong>Notes</strong></p>
<ul>
<li>By default all vehicle specifications from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> are set to
<code>null</code> and the <a href="sdk-for-flutter-explore-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>
is set to <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a>.</li>
<li>A route can be calculated with only the <a href="sdk-for-flutter-explore-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from
<a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> set.</li>
</ul>
<ul>
<li>
<p><code>calculationOptions</code> The options to be used to calculate this isoline.</p>
</li>
<li>
<p><code>routingOptions</code> The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory IsolineOptions.withRoutingOptions(IsolineOptionsCalculation calculationOptions, RoutingOptions routingOptions) =&gt; $prototype.withRoutingOptions(calculationOptions, routingOptions);</code></pre>

 



</div>
`
}</HTMLBlock>
