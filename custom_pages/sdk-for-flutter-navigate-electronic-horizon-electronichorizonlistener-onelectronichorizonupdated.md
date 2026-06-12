---
title: "onElectronicHorizonUpdated abstract method"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-onelectronichorizonupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onElectronicHorizonUpdated.html -->


<div>
<h1>onElectronicHorizonUpdated abstract method</h1></div>

void
onElectronicHorizonUpdated(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>? errorCode, </li>
<li><a href="/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class">ElectronicHorizonUpdate</a>? update</li>
</ol>)

      

    

<p>Called whenever the electronic horizon subsystem produces:</p>
<ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
<p>The client must inspect <code>error_code</code> to determine whether the call
represents an error or a valid update.</p>
<ul>
<li>
<p><code>errorCode</code> The error associated with the horizon computation.
<code>null</code> means no error.</p>
</li>
<li>
<p><code>update</code> The update describing the current electronic horizon state.
May be <code>null</code> if an update could not be produced.</p>
</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onElectronicHorizonUpdated(ElectronicHorizonErrorCode? errorCode, ElectronicHorizonUpdate? update);</code></pre>

 



</div>
`
}</HTMLBlock>
