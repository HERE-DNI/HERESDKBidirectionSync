---
title: "billingTag property"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-billingtag"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- billingTag.html -->


<div>
<h1>billingTag property</h1></div>

        
        String?
        billingTag
<div class="features">getter/setter pair</div>


<p>Internal to HERE SDK. DO NOT USE THIS YET.</p>
<p><strong>Warning:</strong> This is a placeholder and under developement. We will announce its availability in our changelog once it is ready for use.</p>
<p>A parameter to set a billing tag to track your HERE platform usage across the various HERE services your application may contact.
For more information on the billing tag, see our
<a href="https://www.here.com/docs/bundle/cost-management-developer-guide/page/topics/tutorial-billing-tags.html">cost management guide</a>.
The tag needs to follow the format as described in the guide or it will be ignored.
The parameter defaults to <code>null</code>, which also means that the tag is ignored for all requests.</p>
<p><strong>Note:</strong> The billing tag is optional, but when set, it can help you to understand
how often your app uses certain services, for example, the number of hits to our
HERE backend routing services. For more details on tracking such details,
please consult the <em>cost management guide</em> or get in touch with the HERE billing team.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? billingTag;</code></pre>

 



</div>
`
}</HTMLBlock>
