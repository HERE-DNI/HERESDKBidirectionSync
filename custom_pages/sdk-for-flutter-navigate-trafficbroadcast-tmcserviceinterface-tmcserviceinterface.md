---
title: "TMCServiceInterface constructor"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-tmcserviceinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TMCServiceInterface.html -->


<div>
<h1>TMCServiceInterface constructor</h1></div>

TMCServiceInterface(<ol class="parameter-list single-line"> <li>void requestTMCServiceLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcservicerequest-class">TMCServiceRequest</a></li>
</ol>), </li>
<li>List&lt;int&gt; getTMCPreferredSidsLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-trafficbroadcast-tmcpreferredsidsrequest-class">TMCPreferredSidsRequest</a></li>
</ol>), </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class">RDSEncryptionKey</a>&gt; getRDSEncryptionKeysLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkeysrequest-class">RDSEncryptionKeysRequest</a></li>
</ol>)</li>
</ol>)
    

<p>Contains all outgoing dependencies to the client side.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TMCServiceInterface(
  void Function(TMCServiceRequest) requestTMCServiceLambda,
  List&lt;int&gt; Function(TMCPreferredSidsRequest) getTMCPreferredSidsLambda,
  List&lt;RDSEncryptionKey&gt; Function(RDSEncryptionKeysRequest) getRDSEncryptionKeysLambda,

) =&gt; TMCServiceInterface$Lambdas(
  requestTMCServiceLambda,
  getTMCPreferredSidsLambda,
  getRDSEncryptionKeysLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
