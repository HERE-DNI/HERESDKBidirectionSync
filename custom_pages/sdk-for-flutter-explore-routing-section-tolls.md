---
title: "tolls property"
slug: "sdk-for-flutter-explore-routing-section-tolls"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- tolls.html -->


<div>
<h1>tolls property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-explore-routing-toll-class">Toll</a>&gt;
tolls


<p>All the tolls for this section.
Note that tolls are found depending on the transport mode.
For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor
route sections have no tolls, too.
<strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available with the Navigate license. If you're using the
<code>RoutingEngine</code>, this feature is considered to be stable.
Gets all the tolls for this section. Note that tolls are found depending on the
transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls.
Indoor route sections have no tolls, too.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Toll&gt; get tolls;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
