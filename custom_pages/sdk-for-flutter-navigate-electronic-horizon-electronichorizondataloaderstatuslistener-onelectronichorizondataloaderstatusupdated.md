---
title: "onElectronicHorizonDataLoaderStatusUpdated abstract method"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloaderstatuslistener-onelectronichorizondataloaderstatusupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onElectronicHorizonDataLoaderStatusUpdated.html -->


<div>
<h1>onElectronicHorizonDataLoaderStatusUpdated abstract method</h1></div>

void
onElectronicHorizonDataLoaderStatusUpdated(<ol class="parameter-list single-line"> <li>Map&lt;int, <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>&gt; electronicHorizonDataLoaderStatuses</li>
</ol>)

      

    

<p>Called whenever there is a change in the status of the loaded data from <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.</p>
<ul>
<li><code>electronicHorizonDataLoaderStatuses</code> The updated statuses of the loaded data from <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizondataloader-class">ElectronicHorizonDataLoader</a>.
The key is the level of a <code>ElectronicHorizonPath</code>, the value is the current status.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onElectronicHorizonDataLoaderStatusUpdated(Map&lt;int, ElectronicHorizonDataLoadedStatus&gt; electronicHorizonDataLoaderStatuses);</code></pre>

 



</div>
`
}</HTMLBlock>
