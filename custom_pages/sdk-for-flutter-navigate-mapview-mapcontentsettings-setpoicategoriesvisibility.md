---
title: "setPoiCategoriesVisibility static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-setpoicategoriesvisibility"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPoiCategoriesVisibility.html -->


<div>
<h1>setPoiCategoriesVisibility static method</h1></div>

void
setPoiCategoriesVisibility(<ol class="parameter-list single-line"> <li>List&lt;String&gt; categoryIds, </li>
<li><a href="sdk-for-flutter-navigate-mapview-visibilitystate">VisibilityState</a> visibility</li>
</ol>)

      

    

<p>Sets visibility for embedded carto POI categories (points of interest that are visible on the
map, by default).</p>
<p>For HERE standard map schemes all available POI categories are visible by
default for each selected map scheme. Note that not all POI categories are available for
all map schemes.</p>
<p>Based on the given list of categories the number of shown carto POIs can be reduced.
To find all possible POI category strings look into <code>here.sdk.search.PlaceCategory</code>.
Note that it is enough to hide a main category like "100" (eat-and-drink) to also affect
sub categories such as "100-1000" (eat-and-drink-restaurant)
and "100-1100" (eat-and-drink-coffee-tea). To enable a sub category, also the related
main categories need have the <code>VISIBLE</code> state.</p>
<p>The POI visibility is a property of the map data itself. Once set it will be applied to
all HERE standard map schemes and the selected categories will remain even when
switching a map scheme.</p>
<ul>
<li>
<p><code>categoryIds</code> A list of POI categories that a visibility state is set for.</p>
</li>
<li>
<p><code>visibility</code> A selected visibility for specified POI categories.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setPoiCategoriesVisibility(List&lt;String&gt; categoryIds, VisibilityState visibility) =&gt; $prototype.setPoiCategoriesVisibility(categoryIds, visibility);</code></pre>

 



</div>
`
}</HTMLBlock>
