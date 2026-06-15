---
title: "freeResource abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcontext-freeresource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- freeResource.html -->


<div>
<h1>freeResource abstract method</h1></div>

void
freeResource(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapcontextresourcetype">MapContextResourceType</a> type, </li>
<li><a href="sdk-for-flutter-explore-mapview-mapcontextfreeresourceseverity">MapContextFreeResourceSeverity</a> severity</li>
</ol>)

      

    

<p>Frees a system resource held by the <a href="sdk-for-flutter-explore-mapview-mapcontext-class">MapContext</a> and all entities attached to it, like <a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a>.</p>
<p>This function is intended for use when a system resource availability becomes low.
For example, some memory can be freed when the application transitions to the background state.</p>
<ul>
<li>
<p><code>type</code> Type of resource to be freed.</p>
</li>
<li>
<p><code>severity</code> Severity of the request.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void freeResource(MapContextResourceType type, MapContextFreeResourceSeverity severity);</code></pre>

 



</div>
`
}</HTMLBlock>
