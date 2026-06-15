---
title: "getStateCodes abstract method"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-getstatecodes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getStateCodes.html -->


<div>
<h1>getStateCodes abstract method</h1></div>

List&lt;String&gt;
getStateCodes(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-countrycode">CountryCode</a> countryCode</li>
</ol>)

      

    

<p>Synchronously loads the list of state codes from a specified country for which
administrative rules are availabe.</p>
<p>These state codes can then be used to get specific
administrative rules for a specified state using the <code>get_administrative_rules()</code> method.
Returns a list with all the state codes available in the country. In case the country has no
states, the list will be empty.</p>
<ul>
<li><code>countryCode</code> The country code for which the state codes are going to be retrieved.</li>
</ul>
<p>Returns <code>List&lt;String&gt;</code>. The list of state codes present in the country for which administrative rules
are available.</p>
<p>Throws if it's not possible to return the list of state codes.</p>
<p>Throws <a href="sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why the list of state codes was not returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;String&gt; getStateCodes(CountryCode countryCode);</code></pre>

 



</div>
`
}</HTMLBlock>
