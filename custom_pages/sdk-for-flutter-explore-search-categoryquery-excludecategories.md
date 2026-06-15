---
title: "excludeCategories property"
slug: "sdk-for-flutter-explore-search-categoryquery-excludecategories"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- excludeCategories.html -->


<div>
<h1>excludeCategories property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a>&gt;
excludeCategories
<div class="features">getter/setter pair</div>


<p>List of categories and subcategories to be excluded.
A place can be assigned multiple categories. If any of them is in <code>CategoryQuery.excludeCategories</code>,
that place will not be included in the response, regardless of whether any of its assigned
categories have been included in <code>CategoryQuery.categories</code>.
In short, an exclusion will always win over an inclusion.
This is especially useful for excluding specific subcategories from the main category.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;PlaceCategory&gt; excludeCategories;</code></pre>

 



</div>
`
}</HTMLBlock>
