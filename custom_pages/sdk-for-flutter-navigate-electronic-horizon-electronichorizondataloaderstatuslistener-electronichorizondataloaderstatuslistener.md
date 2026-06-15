---
title: "ElectronicHorizonDataLoaderStatusListener constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-electronichorizondataloaderstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonDataLoaderStatusListener.html -->


<div>
<h1>ElectronicHorizonDataLoaderStatusListener constructor</h1></div>

ElectronicHorizonDataLoaderStatusListener(<ol class="parameter-list single-line"> <li>void onElectronicHorizonDataLoaderStatusUpdatedLambda(<ol class="parameter-list single-line"> <li>Map&lt;int, <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>Provides a listener for status updates from the <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-loaddata">ElectronicHorizonDataLoader.loadData</a> method.</p>
<p>The listener receives the current state for different levels of the paths as <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ElectronicHorizonDataLoaderStatusListener(
  void Function(Map&lt;int, ElectronicHorizonDataLoadedStatus&gt;) onElectronicHorizonDataLoaderStatusUpdatedLambda,

) =&gt; ElectronicHorizonDataLoaderStatusListener$Lambdas(
  onElectronicHorizonDataLoaderStatusUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
