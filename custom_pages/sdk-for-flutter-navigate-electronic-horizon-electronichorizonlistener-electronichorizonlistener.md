---
title: "ElectronicHorizonListener constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-electronichorizonlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonListener.html -->


<div>
<h1>ElectronicHorizonListener constructor</h1></div>

ElectronicHorizonListener(<ol class="parameter-list single-line"> <li>void onElectronicHorizonUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>?, </li>
<li><a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a>?</li>
</ol>)</li>
</ol>)
    

<p>Provides a listener for receiving updates during execution of the <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update">ElectronicHorizonEngine.update</a> method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonListener(
  void Function(ElectronicHorizonErrorCode?, ElectronicHorizonUpdate?) onElectronicHorizonUpdatedLambda,

) =&gt; ElectronicHorizonListener$Lambdas(
  onElectronicHorizonUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
