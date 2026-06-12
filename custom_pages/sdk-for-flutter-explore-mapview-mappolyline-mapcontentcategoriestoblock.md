---
title: "mapContentCategoriesToBlock property"
slug: "sdk-for-flutter-explore-mapview-mappolyline-mapcontentcategoriestoblock"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- mapContentCategoriesToBlock.html -->


<div>
<h1>mapContentCategoriesToBlock property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-explore-mapview-mapcontentcategory">MapContentCategory</a>&gt;
mapContentCategoriesToBlock


<p>List of map content categories this polyline should block.
Gets list of map content categories this polyline should block.</p>
<p>Default value is an empty list meaning none of the map categories will be blocked.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;MapContentCategory&gt; get mapContentCategoriesToBlock;</code></pre>

</section>
<section id="setter">

void
mapContentCategoriesToBlock=(List&lt;<a href="/sdk-for-flutter-explore-mapview-mapcontentcategory">MapContentCategory</a>&gt; value)


<p>List of map content categories this polyline should block.
Sets list of map content categories this polyline should block.</p>
<p>Map content categories overlapping the polyline geometry
(progress and non-progress) will be discarded from being rendered.</p>
<p>Duplicate entries will be ignored and will have no additional effect.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set mapContentCategoriesToBlock(List&lt;MapContentCategory&gt; value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
