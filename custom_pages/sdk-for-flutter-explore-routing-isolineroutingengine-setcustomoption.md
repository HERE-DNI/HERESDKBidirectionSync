---
title: "setCustomOption abstract method"
slug: "sdk-for-flutter-explore-routing-isolineroutingengine-setcustomoption"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomOption.html -->


<div>
<h1>setCustomOption abstract method</h1></div>

<a href="sdk-for-flutter-explore-routing-routingerror">RoutingError</a>?
setCustomOption(<ol class="parameter-list single-line"> <li>String name, </li>
<li>String? value</li>
</ol>)

      

    

<p>Sets a custom option for routing backend queries.</p>
<p>The custom option is applied to all the queries that <code>IsolineRoutingEngine</code> performs.
For a complete list of available parameter names and their valid values, refer to
<a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Routing API v8</a>.
<strong>Note:</strong> It's easy to set a wrong option that makes queries invalid,
so make sure you read and understand the backend documentation.</p>
<ul>
<li>
<p><code>name</code> An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.
The option name should't duplicate option names that SDK creates by itself for usage in the query,
otherwise the query will callback with the error <code>RoutingError.INTERNAL_ERROR</code>.</p>
</li>
<li>
<p><code>value</code> An option value. If the value is <code>null</code>, the option will be removed. The option value must be a non-empty string.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError?</a>. An optional error of setting the option.</p>
<p>It's <code>null</code> if the option has been set successfully.
It's <code>RoutingError.INVALID_PARAMETER</code> if the input name and/or value haven't passed internal validation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RoutingError? setCustomOption(String name, String? value);</code></pre>

 



</div>
`
}</HTMLBlock>
