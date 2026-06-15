---
title: "excludeFoodTypes property"
slug: "sdk-for-flutter-navigate-search-categoryquery-excludefoodtypes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- excludeFoodTypes.html -->


<div>
<h1>excludeFoodTypes property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-search-placefoodtype-class">PlaceFoodType</a>&gt;
excludeFoodTypes
<div class="features">getter/setter pair</div>


<p>List of food types to be excluded.
A place can be assigned multiple food types. If any of them is in <code>CategoryQuery.excludeFoodTypes</code>,
that place will not be included in the response, regardless of whether any of its assigned
food types have been included in <code>CategoryQuery.includeFoodTypes</code>.
In short, an exclusion will always win over an inclusion.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;PlaceFoodType&gt; excludeFoodTypes;</code></pre>

 



</div>
`
}</HTMLBlock>
