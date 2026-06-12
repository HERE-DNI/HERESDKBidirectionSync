---
title: "PlaceCategory constructor"
slug: "sdk-for-flutter-navigate-search-placecategory-placecategory"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceCategory.html -->


<div>
<h1>PlaceCategory constructor</h1></div>

PlaceCategory(<ol class="parameter-list single-line"> <li>String id</li>
</ol>)
    

<p>Creates a new instance of this class.</p>
<ul>
<li><code>id</code> Place category ID.
The HERE places category system provides three levels of granularity:</li>
</ul>
<ol>
<li>Level 1 represents high level groupings, such as "Eat and drink".
Their IDs take the form "xxx", for example "100".</li>
<li>Level 2 represents logical sub-groups or domains, such as "Eat and Drink / Restaurant".
Their IDs take the form "xxx-xxxx", for example "100-1000".</li>
<li>Level 3 provides the greatest level of granularity about place categorization,
such as "Eat and Drink / Restaurant / Casual Dining".
Their IDs take the form "xxx-xxxx-xxxx", for example "100-1000-0001".
The category ID can be provided as one of the predefined values, such as
<a href="/sdk-for-flutter-navigate-search-placecategory-eatanddrinkrestaurant">PlaceCategory.eatAndDrinkRestaurant</a> or as a literal string that matches
one of the category IDs defined by the HERE Search service.
Only level 1 and 2 category IDs are predefined.
The complete list of supported category IDs, including level 3, can be found online:
<a href="https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html">https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html</a>.</li>
</ol>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PlaceCategory(String id) =&gt; $prototype.make(id);</code></pre>

 



</div>
`
}</HTMLBlock>
