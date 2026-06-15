---
title: "internalsetCallListenerFromMainThreadEnabled method"
slug: "sdk-for-flutter-navigate-location-locationengine-internalsetcalllistenerfrommainthreadenabled"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- internalsetCallListenerFromMainThreadEnabled.html -->


<div>
<h1>internalsetCallListenerFromMainThreadEnabled method</h1></div>

void
internalsetCallListenerFromMainThreadEnabled(<ol class="parameter-list single-line"> <li>bool enabled</li>
</ol>)

      

    

<p>Enables or disables forcing listener calls to originate from main thread.</p>
<p>When disabled listener calls can originate from any thread.
Defaults to false .</p>
<p>For internal use only.</p>
<ul>
<li><code>enabled</code> The enabled flag.</li>
</ul>
<p>@nodoc</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void internalsetCallListenerFromMainThreadEnabled(bool enabled) =&gt;
    _location.internalsetCallListenerFromMainThreadEnabled(enabled);</code></pre>

 



</div>
`
}</HTMLBlock>
