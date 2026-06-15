---
title: "EmailAddress constructor"
slug: "sdk-for-flutter-navigate-search-emailaddress-emailaddress"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EmailAddress.html -->


<div>
<h1>EmailAddress constructor</h1></div>

EmailAddress(<ol class="parameter-list single-line"> <li>String address, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a>&gt; categories</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>address</code> The email address.</li>
<li><code>categories</code> Categories associated with email address.
Note: In case <a href="sdk-for-flutter-navigate-search-emailaddress-categories">EmailAddress.categories</a> are not empty, then <a href="sdk-for-flutter-navigate-search-emailaddress-address">EmailAddress.address</a> should be used according to given categories.
Otherwise, <a href="sdk-for-flutter-navigate-search-emailaddress-address">EmailAddress.address</a> is meant for general use.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EmailAddress(this.address, this.categories);</code></pre>

 



</div>
`
}</HTMLBlock>
