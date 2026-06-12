---
title: "getTMCPreferredSids abstract method"
slug: "sdk-for-flutter-navigate-trafficbroadcast-tmcserviceinterface-gettmcpreferredsids"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getTMCPreferredSids.html -->


<div>
<h1>getTMCPreferredSids abstract method</h1></div>

List&lt;int&gt;
getTMCPreferredSids(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-trafficbroadcast-tmcpreferredsidsrequest-class">TMCPreferredSidsRequest</a> tmcPreferredSidsRequest</li>
</ol>)

      

    

<p>Called whenever there is a need to get a list of preferred SIDs for a specific area.</p>
<ul>
<li><code>tmcPreferredSidsRequest</code> Specifies the area to request the preferred SIDs.</li>
</ul>
<p>Returns <code>List&lt;int&gt;</code>. List of preferred SIDs.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;int&gt; getTMCPreferredSids(TMCPreferredSidsRequest tmcPreferredSidsRequest);</code></pre>

 



</div>
`
}</HTMLBlock>
