---
title: "diffBetweenVideoMemoryLimitAndRequirementInKiB property"
slug: "sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementresult-diffbetweenvideomemorylimitandrequirementinkib"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- diffBetweenVideoMemoryLimitAndRequirementInKiB.html -->


<div>
<h1>diffBetweenVideoMemoryLimitAndRequirementInKiB property</h1></div>

        
        int?
        diffBetweenVideoMemoryLimitAndRequirementInKiB
<div class="features">getter/setter pair</div>


<p>The difference in kibibytes between the limit and the video-memory requirement
for only the currently visible data. If positive, the returned value is the surplus
value over the currently required bare minimum. Even when positive, if the limit set
is low, the application could later breach the limit and delete even visible data.
A non positive value means the limit cannot fit the existing visible data and there could
be data disappearing or flickering. If for some reason the callback is ignored or
correct memory limit cannot be calculated, <code>null</code> value is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? diffBetweenVideoMemoryLimitAndRequirementInKiB;</code></pre>

 



</div>
`
}</HTMLBlock>
