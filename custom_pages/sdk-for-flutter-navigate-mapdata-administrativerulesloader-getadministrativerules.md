---
title: "getAdministrativeRules abstract method"
slug: "sdk-for-flutter-navigate-mapdata-administrativerulesloader-getadministrativerules"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getAdministrativeRules.html -->


<div>
<h1>getAdministrativeRules abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a>
getAdministrativeRules(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-countrycode">CountryCode</a> countryCode, </li>
<li>String? stateCode</li>
</ol>)

      

    

<p>Synchronously load the administrative rules for the specified country and state.</p>
<p><strong>Note:</strong> The <code>state_code</code> parameter can be set to <code>null</code>. In this case, even if the country has multiple states, each with
their own administrative rules, an <a href="/sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a> object will be returned, containing the administrative
rules valid for the entire country. These rules can however be overwritten by the state rules when the driver is in that
specific state, so it is recommended to always retrieve the rules for a specific state for higher accuracy.
Returns an <a href="/sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a> object which contains the administrative rules for the specified country and
state.</p>
<ul>
<li>
<p><code>countryCode</code> The country code for which the administrative rules will be retrieved.</p>
</li>
<li>
<p><code>stateCode</code> The state name for which the administrative rules will be received. It can be <code>null</code>.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapdata-administrativerules-class">AdministrativeRules</a>. Requested administrative rules for the country and the state specified.</p>
<p>Throws <a href="/sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class">MapDataLoaderExceptionException</a>. Specifies reason, why the administrative rules were not retrieved.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">AdministrativeRules getAdministrativeRules(CountryCode countryCode, String? stateCode);</code></pre>

 



</div>
`
}</HTMLBlock>
