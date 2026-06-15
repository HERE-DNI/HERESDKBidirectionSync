---
title: "getRDSEncryptionKeys abstract method"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-getrdsencryptionkeys"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getRDSEncryptionKeys.html -->


<div>
<h1>getRDSEncryptionKeys abstract method</h1></div>

List&lt;<a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkey-class">RDSEncryptionKey</a>&gt;
getRDSEncryptionKeys(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-trafficbroadcast-rdsencryptionkeysrequest-class">RDSEncryptionKeysRequest</a> rdsEncryptionKeysRequest</li>
</ol>)

      

    

<p>Called whenever there is a need to get RDS encryption keys.</p>
<ul>
<li><code>rdsEncryptionKeysRequest</code> Input data to search for keys.</li>
</ul>
<p>Returns <code>List&lt;RDSEncryptionKey&gt;</code>. RDS encryption keys.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;RDSEncryptionKey&gt; getRDSEncryptionKeys(RDSEncryptionKeysRequest rdsEncryptionKeysRequest);</code></pre>

 



</div>
`
}</HTMLBlock>
