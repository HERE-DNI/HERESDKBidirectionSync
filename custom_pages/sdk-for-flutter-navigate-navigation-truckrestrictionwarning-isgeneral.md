---
title: "isGeneral method"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionwarning-isgeneral"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isGeneral.html -->


<div>
<h1>isGeneral method</h1></div>

bool
isGeneral()

      

    

<p>Checks if this truck restriction warning is general.</p>
<p>A general warning has no specific restriction conditions set.
Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition.
This method only checks that no specific conditions are set for the warning.</p>
<p>Returns <code>bool</code>. <code>true</code> if all restriction fields are null or empty, <code>false</code> otherwise.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool isGeneral() =&gt; $prototype.isGeneral(this);</code></pre>

 



</div>
`
}</HTMLBlock>
