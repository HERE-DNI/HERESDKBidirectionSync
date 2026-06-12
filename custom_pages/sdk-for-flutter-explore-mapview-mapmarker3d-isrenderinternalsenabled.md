---
title: "isRenderInternalsEnabled property"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-isrenderinternalsenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isRenderInternalsEnabled.html -->


<div>
<h1>isRenderInternalsEnabled property</h1></div>
<section id="getter">

bool
isRenderInternalsEnabled


<p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.
Default value is <code>false</code>. Can be used with translucent 3D marker.</p>
<p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
passes: first pass with front-face, second pass with back-face culling enabled.
With this flag enabled for 3D marker with depth check disabled rendering is performed in a
single pass with back-face culling disabled.
Returns a flag indicating whether to render internal geometry of a 3D marker occluded by its front
facing polygons. Default value is <code>false</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isRenderInternalsEnabled;</code></pre>

</section>
<section id="setter">

void
isRenderInternalsEnabled=(bool value)


<p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.
Default value is <code>false</code>. Can be used with translucent 3D marker.</p>
<p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
passes: first pass with front-face, second pass with back-face culling enabled.
With this flag enabled for 3D marker with depth check disabled rendering is performed in a
single pass with back-face culling disabled.
Sets a flag indicating whether to render internal geometry of a 3D marker occluded by its front
facing polygons.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isRenderInternalsEnabled(bool value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
