---
title: "MapLoader  Reference"
slug: "sdk-for-ios-explore-maploader"
---

<span id="//apple_ref/swift/Section/MapLoader" class="dashAnchor"></span>

<div class="content-wrapper">

<a href="sdk-for-ios-explore-index">heresdk</a> <img src="img/carat.png" id="sdk-for-ios-explore-carat" /> MapLoader Reference

</div>

<div class="content-wrapper">

<nav class="sidebar">

- <a href="sdk-for-ios-explore-core">Core</a>
  - <a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a>
  - <a href="sdk-for-ios-explore-structs-anchor2dkeyframe">Anchor2DKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-angle">Angle</a>
  - <a href="sdk-for-ios-explore-structs-anglerange">AngleRange</a>
  - <a href="sdk-for-ios-explore-classes-authentication">Authentication</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk23AuthenticationExceptiona">AuthenticationException</a>
  - <a href="sdk-for-ios-explore-classes-authenticationmode">AuthenticationMode</a>
  - <a href="sdk-for-ios-explore-structs-brandlogo">BrandLogo</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk30CacheCallbackCompletionHandlera">CacheCallbackCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-cardinaldirection">CardinalDirection</a>
  - <a href="sdk-for-ios-explore-structs-catalogconfiguration">CatalogConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-catalogidentifier">CatalogIdentifier</a>
  - <a href="sdk-for-ios-explore-enums-catalogtype">CatalogType</a>
  - <a href="sdk-for-ios-explore-classes-catalogupdatetask">CatalogUpdateTask</a>
  - <a href="sdk-for-ios-explore-classes-catalogversionhint">CatalogVersionHint</a>
  - <a href="sdk-for-ios-explore-classes-collectionof">CollectionOf</a>
  - <a href="sdk-for-ios-explore-enums-countrycode">CountryCode</a>
  - <a href="sdk-for-ios-explore-enums-currenttype">CurrentType</a>
  - <a href="sdk-for-ios-explore-protocols-custommetadatavalue">CustomMetadataValue</a>
  - <a href="sdk-for-ios-explore-structs-desiredcatalog">DesiredCatalog</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk14DeviceIdHandlea">DeviceIdHandle</a>
  - <a href="sdk-for-ios-explore-enums-enginebaseurl">EngineBaseURL</a>
  - <a href="sdk-for-ios-explore-structs-engineoptions">EngineOptions</a>
  - <a href="sdk-for-ios-explore-structs-externalid">ExternalID</a>
  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-geocircle">GeoCircle</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-explore-structs-geocorridor">GeoCorridor</a>
  - <a href="sdk-for-ios-explore-structs-geoorientation">GeoOrientation</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-explore-structs-geopolygon">GeoPolygon</a>
  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>
  - <a href="sdk-for-ios-explore-enums-geopolylinedirection">GeoPolylineDirection</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk18InstantiationErrora">InstantiationError</a>
  - <a href="sdk-for-ios-explore-enums-instantiationerrorcode">InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-integerrange">IntegerRange</a>
  - <a href="sdk-for-ios-explore-enums-junctionstraversability">JunctionsTraversability</a>
  - <a href="sdk-for-ios-explore-enums-languagecode">LanguageCode</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration">LayerConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-layerconfiguration-feature">– Feature</a>
  - <a href="sdk-for-ios-explore-structs-localizedroadnumber">LocalizedRoadNumber</a>
  - <a href="sdk-for-ios-explore-structs-localizedroadnumbers">LocalizedRoadNumbers</a>
  - <a href="sdk-for-ios-explore-structs-localizedtext">LocalizedText</a>
  - <a href="sdk-for-ios-explore-structs-localizedtexts">LocalizedTexts</a>
  - <a href="sdk-for-ios-explore-structs-location">Location</a>
  - <a href="sdk-for-ios-explore-protocols-locationdelegate">LocationDelegate</a>
  - <a href="sdk-for-ios-explore-enums-locationsource">LocationSource</a>
  - <a href="sdk-for-ios-explore-enums-locationtechnology">LocationTechnology</a>
  - <a href="sdk-for-ios-explore-structs-locationtime">LocationTime</a>
  - <a href="sdk-for-ios-explore-protocols-logappender">LogAppender</a>
  - <a href="sdk-for-ios-explore-classes-logcontrol">LogControl</a>
  - <a href="sdk-for-ios-explore-enums-loglevel">LogLevel</a>
  - <a href="sdk-for-ios-explore-classes-metadata">Metadata</a>
  - <a href="sdk-for-ios-explore-enums-metadatatype">MetadataType</a>
  - <a href="sdk-for-ios-explore-structs-nameid">NameID</a>
  - <a href="sdk-for-ios-explore-structs-networkendpoint">NetworkEndpoint</a>
  - <a href="sdk-for-ios-explore-structs-networksettings">NetworkSettings</a>
  - <a href="sdk-for-ios-explore-structs-parameterconfiguration">ParameterConfiguration</a>
  - <a href="sdk-for-ios-explore-enums-passthroughfeature">PassThroughFeature</a>
  - <a href="sdk-for-ios-explore-enums-powertype">PowerType</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianprofile">PedestrianProfile</a>
  - <a href="sdk-for-ios-explore-structs-pickedplace">PickedPlace</a>
  - <a href="sdk-for-ios-explore-protocols-platformthreading">PlatformThreading</a>
  - <a href="sdk-for-ios-explore-structs-point2d">Point2D</a>
  - <a href="sdk-for-ios-explore-structs-point3d">Point3D</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-polylinesimplificationerror">PolylineSimplificationError</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier">PolylineSimplifier</a>
  - <a href="sdk-for-ios-explore-classes-polylinesimplifier-options">– Options</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings">ProxySettings</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings-proxytype">– ProxyType</a>
  - <a href="sdk-for-ios-explore-structs-proxysettings-credentials">– Credentials</a>
  - <a href="sdk-for-ios-explore-structs-rectangle2d">Rectangle2D</a>
  - <a href="sdk-for-ios-explore-enums-routetype">RouteType</a>
  - <a href="sdk-for-ios-explore-protocols-runnable">Runnable</a>
  - <a href="sdk-for-ios-explore-classes-sdkbuildinformation">SDKBuildInformation</a>
  - <a href="sdk-for-ios-explore-classes-sdkcache">SDKCache</a>
  - <a href="sdk-for-ios-explore-classes-sdkinternalinitializer">SDKInternalInitializer</a>
  - <a href="sdk-for-ios-explore-classes-sdklogger">SDKLogger</a>
  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-classes-sdknativeengine-purgememorystrategy">– PurgeMemoryStrategy</a>
  - <a href="sdk-for-ios-explore-core#/c:@M@heresdk@objc(cs">SDKNativeEngineHolder</a>SDKNativeEngineHolder)
  - <a href="sdk-for-ios-explore-structs-sdkoptions">SDKOptions</a>
  - <a href="sdk-for-ios-explore-structs-sdkversion">SDKVersion</a>
  - <a href="sdk-for-ios-explore-structs-size2d">Size2D</a>
  - <a href="sdk-for-ios-explore-core#/s:SS">String</a>
  - <a href="sdk-for-ios-explore-core#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>
  - <a href="sdk-for-ios-explore-enums-taskoutcome">TaskOutcome</a>
  - <a href="sdk-for-ios-explore-classes-threading">Threading</a>
  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>
  - <a href="sdk-for-ios-explore-structs-transportprofile">TransportProfile</a>
  - <a href="sdk-for-ios-explore-extensions-uicolor">UIColor</a>
  - <a href="sdk-for-ios-explore-enums-unitsystem">UnitSystem</a>
  - <a href="sdk-for-ios-explore-structs-usagestats">UsageStats</a>
  - <a href="sdk-for-ios-explore-structs-usagestats-feature">– Feature</a>
  - <a href="sdk-for-ios-explore-structs-usagestats-networkstats">– NetworkStats</a>
- <a href="sdk-for-ios-explore-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-explore-classes-electronichorizondataloader">ElectronicHorizonDataLoader</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizondataloaderresult">ElectronicHorizonDataLoaderResult</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a>
  - <a href="sdk-for-ios-explore-protocols-electronichorizondataloaderstatusdelegate">ElectronicHorizonDataLoaderStatusDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a>
  - <a href="sdk-for-ios-explore-classes-electronichorizonengine">ElectronicHorizonEngine</a>
  - <a href="sdk-for-ios-explore-enums-electronichorizonerrorcode">ElectronicHorizonErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonoptions">ElectronicHorizonOptions</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonpath">ElectronicHorizonPath</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonposition">ElectronicHorizonPosition</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegment">ElectronicHorizonSegment</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonsegmentid">ElectronicHorizonSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-electronichorizonupdate">ElectronicHorizonUpdate</a>
- <a href="sdk-for-ios-explore-ev">EV</a>
  - <a href="sdk-for-ios-explore-enums-evchargingconnectorformat">EVChargingConnectorFormat</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectortype">EVChargingConnectorType</a>
  - <a href="sdk-for-ios-explore-enums-evsecapability">EVSECapability</a>
  - <a href="sdk-for-ios-explore-enums-evsepaymentsupport">EVSEPaymentSupport</a>
  - <a href="sdk-for-ios-explore-enums-evsestate">EVSEState</a>
- <a href="sdk-for-ios-explore-positioning">Positioning</a>
  - <a href="sdk-for-ios-explore-structs-authenticationdata">AuthenticationData</a>
  - <a href="sdk-for-ios-explore-enums-authenticationerror">AuthenticationError</a>
  - <a href="sdk-for-ios-explore-enums-confirmationstatus">ConfirmationStatus</a>
  - <a href="sdk-for-ios-explore-enums-locationaccuracy">LocationAccuracy</a>
  - <a href="sdk-for-ios-explore-protocols-locationenginebase">LocationEngineBase</a>
  - <a href="sdk-for-ios-explore-enums-locationenginestatus">LocationEngineStatus</a>
  - <a href="sdk-for-ios-explore-enums-locationfeature">LocationFeature</a>
  - <a href="sdk-for-ios-explore-classes-locationengine">LocationEngine</a>
  - <a href="sdk-for-ios-explore-classes-locationsimulator">LocationSimulator</a>
  - <a href="sdk-for-ios-explore-structs-locationsimulatoroptions">LocationSimulatorOptions</a>
  - <a href="sdk-for-ios-explore-protocols-locationstatusdelegate">LocationStatusDelegate</a>
- <a href="sdk-for-ios-explore-mapdata">MapData</a>
  - <a href="sdk-for-ios-explore-structs-administrativerules">AdministrativeRules</a>
  - <a href="sdk-for-ios-explore-classes-administrativerulesloader">AdministrativeRulesLoader</a>
  - <a href="sdk-for-ios-explore-structs-allowedtransportmodes">AllowedTransportModes</a>
  - <a href="sdk-for-ios-explore-structs-bloodalcoholcontentlimit">BloodAlcoholContentLimit</a>
  - <a href="sdk-for-ios-explore-structs-connectivity">Connectivity</a>
  - <a href="sdk-for-ios-explore-structs-directedocmsegmentid">DirectedOCMSegmentId</a>
  - <a href="sdk-for-ios-explore-structs-downloadingfileoptions">DownloadingFileOptions</a>
  - <a href="sdk-for-ios-explore-enums-drivingside">DrivingSide</a>
  - <a href="sdk-for-ios-explore-structs-filereference">FileReference</a>
  - <a href="sdk-for-ios-explore-enums-filereferencetype">FileReferenceType</a>
  - <a href="sdk-for-ios-explore-enums-headlightsrequirement">HeadlightsRequirement</a>
  - <a href="sdk-for-ios-explore-structs-laneattribute">LaneAttribute</a>
  - <a href="sdk-for-ios-explore-enums-localroadcharacteristic">LocalRoadCharacteristic</a>
  - <a href="sdk-for-ios-explore-mapdata#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a>
  - <a href="sdk-for-ios-explore-enums-mapdataloadererrorcode">MapDataLoaderErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-ocmsegmentid">OCMSegmentId</a>
  - <a href="sdk-for-ios-explore-enums-parkingsideregulation">ParkingSideRegulation</a>
  - <a href="sdk-for-ios-explore-structs-physicalattributes">PhysicalAttributes</a>
  - <a href="sdk-for-ios-explore-structs-pretripplanning">PreTripPlanning</a>
  - <a href="sdk-for-ios-explore-structs-railwaycrossing">RailwayCrossing</a>
  - <a href="sdk-for-ios-explore-enums-railwaycrossingtype">RailwayCrossingType</a>
  - <a href="sdk-for-ios-explore-enums-roaddivider">RoadDivider</a>
  - <a href="sdk-for-ios-explore-structs-roadusages">RoadUsages</a>
  - <a href="sdk-for-ios-explore-structs-segmentconnectivities">SegmentConnectivities</a>
  - <a href="sdk-for-ios-explore-classes-segmentdata">SegmentData</a>
  - <a href="sdk-for-ios-explore-classes-segmentdataloader">SegmentDataLoader</a>
  - <a href="sdk-for-ios-explore-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a>
  - <a href="sdk-for-ios-explore-classes-segmentreferenceconverter">SegmentReferenceConverter</a>
  - <a href="sdk-for-ios-explore-classes-segmentspandata">SegmentSpanData</a>
  - <a href="sdk-for-ios-explore-structs-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a>
  - <a href="sdk-for-ios-explore-structs-segmentspeedlimit">SegmentSpeedLimit</a>
  - <a href="sdk-for-ios-explore-enums-specialspeedtype">SpecialSpeedType</a>
  - <a href="sdk-for-ios-explore-structs-tollcost">TollCost</a>
  - <a href="sdk-for-ios-explore-structs-tollpoint">TollPoint</a>
  - <a href="sdk-for-ios-explore-structs-tollstructure">TollStructure</a>
  - <a href="sdk-for-ios-explore-structs-tollstructuremaneuver">TollStructureManeuver</a>
  - <a href="sdk-for-ios-explore-enums-tollstructuretype">TollStructureType</a>
  - <a href="sdk-for-ios-explore-structs-tollsystem">TollSystem</a>
  - <a href="sdk-for-ios-explore-structs-trafficsignal">TrafficSignal</a>
  - <a href="sdk-for-ios-explore-enums-trafficsignallocation">TrafficSignalLocation</a>
  - <a href="sdk-for-ios-explore-enums-turnonredregulation">TurnOnRedRegulation</a>
- <a href="sdk-for-ios-explore-maploader">MapLoader</a>
  - <a href="sdk-for-ios-explore-structs-catalogupdateinfo">CatalogUpdateInfo</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a>
  - <a href="sdk-for-ios-explore-protocols-catalogupdateprogresslistener">CatalogUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-enums-catalogupdatestate">CatalogUpdateState</a>
  - <a href="sdk-for-ios-explore-enums-clientcertificaterequesttype">ClientCertificateRequestType</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk17CompletionHandlera">CompletionHandler</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk25ConfigureConnectionHandlea">ConfigureConnectionHandle</a>
  - <a href="sdk-for-ios-explore-protocols-dataattributesbase">DataAttributesBase</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk30DeleteRegionsCompletionHandlera">DeleteRegionsCompletionHandler</a>
  - <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener">DownloadRegionsStatusListener</a>
  - <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient">ExternalMapDataSourceClient</a>
  - <a href="sdk-for-ios-explore-enums-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk35ExternalMapDataSourceExceptionErrora">ExternalMapDataSourceExceptionError</a>
  - <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver">ExternalMapDataSourceServer</a>
  - <a href="sdk-for-ios-explore-structs-installedcatalog">InstalledCatalog</a>
  - <a href="sdk-for-ios-explore-structs-installedregion">InstalledRegion</a>
  - <a href="sdk-for-ios-explore-enums-installedregionstatus">InstalledRegionStatus</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC">LineData</a>
  - <a href="sdk-for-ios-explore-classes-linedataaccessor">LineDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-linedatabuilder">LineDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-linedatasource">LineDataSource</a>
  - <a href="sdk-for-ios-explore-classes-linedatasourcebuilder">LineDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-enums-maploadererror">MapLoaderError</a>
  - <a href="sdk-for-ios-explore-classes-mapdownloader">MapDownloader</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk31MapDownloaderConstructionHandlea">MapDownloaderConstructionHandle</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk18MapLoaderExceptiona">MapLoaderException</a>
  - <a href="sdk-for-ios-explore-classes-mapdownloadertask">MapDownloaderTask</a>
  - <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">MapUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-classes-mapupdater">MapUpdater</a>
  - <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy">– MapUpdateVersionCommitPolicy</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a>
  - <a href="sdk-for-ios-explore-classes-mapupdatetask">MapUpdateTask</a>
  - <a href="sdk-for-ios-explore-classes-mapversionhandle">MapVersionHandle</a>
  - <a href="sdk-for-ios-explore-enums-navigabilitytype">NavigabilityType</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk25OfflineStorageSizeHandlera">OfflineStorageSizeHandler</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk23RepairCompletionHandlera">RepairCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-pemkeycertpair">PemKeyCertPair</a>
  - <a href="sdk-for-ios-explore-enums-persistentmaprepairerror">PersistentMapRepairError</a>
  - <a href="sdk-for-ios-explore-enums-persistentmapstatus">PersistentMapStatus</a>
  - <a href="sdk-for-ios-explore-structs-region">Region</a>
  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>
  - <a href="sdk-for-ios-explore-maploader#/s:7heresdk19ServerStartedHandlea">ServerStartedHandle</a>
  - <a href="sdk-for-ios-explore-structs-sslclientcredentialsoptions">SslClientCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-structs-sslservercredentialsoptions">SslServerCredentialsOptions</a>
  - <a href="sdk-for-ios-explore-structs-updatestatistics">UpdateStatistics</a>
- <a href="sdk-for-ios-explore-mapmatcher">MapMatcher</a>
  - <a href="sdk-for-ios-explore-classes-mapmatcher">MapMatcher</a>
  - <a href="sdk-for-ios-explore-structs-matchedlocation">MatchedLocation</a>
- <a href="sdk-for-ios-explore-maps">Maps</a>
  - <a href="sdk-for-ios-explore-protocols-animationdelegate">AnimationDelegate</a>
  - <a href="sdk-for-ios-explore-enums-animationstate">AnimationState</a>
  - <a href="sdk-for-ios-explore-classes-assetsmanager">AssetsManager</a>
  - <a href="sdk-for-ios-explore-classes-dataattributes">DataAttributes</a>
  - <a href="sdk-for-ios-explore-classes-dataattributesaccessor">DataAttributesAccessor</a>
  - <a href="sdk-for-ios-explore-classes-dataattributesbuilder">DataAttributesBuilder</a>
  - <a href="sdk-for-ios-explore-classes-dataattributevalue">DataAttributeValue</a>
  - <a href="sdk-for-ios-explore-classes-dataattributevalue-valuetype">– ValueType</a>
  - <a href="sdk-for-ios-explore-structs-dashpattern">DashPattern</a>
  - <a href="sdk-for-ios-explore-protocols-doubletapdelegate">DoubleTapDelegate</a>
  - <a href="sdk-for-ios-explore-enums-drawordertype">DrawOrderType</a>
  - <a href="sdk-for-ios-explore-classes-easing">Easing</a>
  - <a href="sdk-for-ios-explore-classes-easing-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-enums-easingfunction">EasingFunction</a>
  - <a href="sdk-for-ios-explore-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationkeyframe">GeoOrientationKeyframe</a>
  - <a href="sdk-for-ios-explore-enums-gesturestate">GestureState</a>
  - <a href="sdk-for-ios-explore-enums-gesturetype">GestureType</a>
  - <a href="sdk-for-ios-explore-classes-gestures">Gestures</a>
  - <a href="sdk-for-ios-explore-classes-heremap">HereMap</a>
  - <a href="sdk-for-ios-explore-classes-iconprovider">IconProvider</a>
  - <a href="sdk-for-ios-explore-enums-iconproviderassettype">IconProviderAssetType</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk20IconProviderCallbacka">IconProviderCallback</a>
  - <a href="sdk-for-ios-explore-enums-iconprovidererror">IconProviderError</a>
  - <a href="sdk-for-ios-explore-enums-imageformat">ImageFormat</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory">JsonStyleFactory</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>
  - <a href="sdk-for-ios-explore-enums-linecap">LineCap</a>
  - <a href="sdk-for-ios-explore-classes-linetiledatasource">LineTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-linetilesource">LineTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-linetilesourceloadresulthandler">LineTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator">LocationIndicator</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator-indicatorstyle">– IndicatorStyle</a>
  - <a href="sdk-for-ios-explore-classes-locationindicator-markertype">– MarkerType</a>
  - <a href="sdk-for-ios-explore-protocols-longpressdelegate">LongPressDelegate</a>
  - <a href="sdk-for-ios-explore-classes-maparrow">MapArrow</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera">MapCamera</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera-state">– State</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera-farplaneconfiguration">– FarPlaneConfiguration</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraanimationfactory">MapCameraAnimationFactory</a>
  - <a href="sdk-for-ios-explore-protocols-mapcameradelegate">MapCameraDelegate</a>
  - <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
  - <a href="sdk-for-ios-explore-classes-mapcamerakeyframetrack-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameralimits">MapCameraLimits</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdate">MapCameraUpdate</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdate-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcameraupdatefactory">MapCameraUpdateFactory</a>
  - <a href="sdk-for-ios-explore-enums-mapcontentcategory">MapContentCategory</a>
  - <a href="sdk-for-ios-explore-classes-mapcontentsettings">MapContentSettings</a>
  - <a href="sdk-for-ios-explore-classes-mapcontentsettings-trafficrefreshperioderrorcode">– TrafficRefreshPeriodErrorCode</a>
  - <a href="sdk-for-ios-explore-enums-mapcontenttype">MapContentType</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext">MapContext</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementstrategy">– MemoryManagementStrategy</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresultcode">– MemoryManagementResultCode</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-resourcetype">– ResourceType</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-freeresourceseverity">– FreeResourceSeverity</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementresult">– MemoryManagementResult</a>
  - <a href="sdk-for-ios-explore-classes-mapcontext-memorymanagementoptions">– MemoryManagementOptions</a>
  - <a href="sdk-for-ios-explore-enums-maperror">MapError</a>
  - <a href="sdk-for-ios-explore-structs-mapfeatures">MapFeatures</a>
  - <a href="sdk-for-ios-explore-structs-mapfeaturemodes">MapFeatureModes</a>
  - <a href="sdk-for-ios-explore-protocols-mapidledelegate">MapIdleDelegate</a>
  - <a href="sdk-for-ios-explore-classes-mapimage">MapImage</a>
  - <a href="sdk-for-ios-explore-classes-mapimageoverlay">MapImageOverlay</a>
  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a>
  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-maplayer">MapLayer</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder">MapLayerBuilder</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-maplayerbuilder-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk16MapLayerPriorityC">MapLayerPriority</a>
  - <a href="sdk-for-ios-explore-classes-maplayerprioritybuilder">MapLayerPriorityBuilder</a>
  - <a href="sdk-for-ios-explore-classes-maplayermapmeasuredependentstoragelevels">MapLayerMapMeasureDependentStorageLevels</a>
  - <a href="sdk-for-ios-explore-structs-maplayervisibilityrange">MapLayerVisibilityRange</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster">MapMarkerCluster</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-grouping">– Grouping</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-imagestyle">– ImageStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkercluster-counterstyle">– CounterStyle</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasurerange">MapMeasureRange</a>
  - <a href="sdk-for-ios-explore-classes-mapobjectdescriptor">MapObjectDescriptor</a>
  - <a href="sdk-for-ios-explore-enums-mapprojection">MapProjection</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights">MapSceneLights</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-category">– Category</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-attributesettingerror">– AttributeSettingError</a>
  - <a href="sdk-for-ios-explore-classes-mapscenelights-direction">– Direction</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapsceneloadoptionsbuilder-instantiationerrordetails">– InstantiationErrorDetails</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker">MapMarker</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker-textstyle">– TextStyle</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3d">MapMarker3D</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3dmodel">MapMarker3DModel</a>
  - <a href="sdk-for-ios-explore-classes-mapmarker3dmodel-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkeranimation">MapMarkerAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mapmarkeranimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure-kind">– Kind</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mappolygon">MapPolygon</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">– Representation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation">– DashImageRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-solidrepresentation">– SolidRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation">– DashRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-solidmulticolorrepresentation">– SolidMultiColorRepresentation</a>
  - <a href="sdk-for-ios-explore-classes-mappolylineanimation">MapPolylineAnimation</a>
  - <a href="sdk-for-ios-explore-classes-mappolylineanimation-instantiationerrorcode">– InstantiationErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-mappickresult">MapPickResult</a>
  - <a href="sdk-for-ios-explore-classes-mapscene">MapScene</a>
  - <a href="sdk-for-ios-explore-classes-mapscene-mappickfilter">– MapPickFilter</a>
  - <a href="sdk-for-ios-explore-enums-mapscheme">MapScheme</a>
  - <a href="sdk-for-ios-explore-protocols-mapviewbase">MapViewBase</a>
  - <a href="sdk-for-ios-explore-classes-mapview">MapView</a>
  - <a href="sdk-for-ios-explore-classes-mapview-viewpin">– ViewPin</a>
  - <a href="sdk-for-ios-explore-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-structs-mapviewoptions">MapViewOptions</a>
  - <a href="sdk-for-ios-explore-structs-materialreflectivity">MaterialReflectivity</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk4MeshC">Mesh</a>
  - <a href="sdk-for-ios-explore-classes-meshbuilder">MeshBuilder</a>
  - <a href="sdk-for-ios-explore-protocols-pandelegate">PanDelegate</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult">PickMapContentResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult-trafficincidentresult">– TrafficIncidentResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapcontentresult-vehiclerestrictionresult">– VehicleRestrictionResult</a>
  - <a href="sdk-for-ios-explore-classes-pickmapitemsresult">PickMapItemsResult</a>
  - <a href="sdk-for-ios-explore-protocols-pinchrotatedelegate">PinchRotateDelegate</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk9PointDataC">PointData</a>
  - <a href="sdk-for-ios-explore-classes-pointdataaccessor">PointDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-pointdatabuilder">PointDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-pointdatasource">PointDataSource</a>
  - <a href="sdk-for-ios-explore-classes-pointdatasourcebuilder">PointDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-classes-pointtiledatasource">PointTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-pointtilesource">PointTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-pointtilesourceloadresulthandler">PointTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-structs-point2dkeyframe">Point2DKeyframe</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk11PolygonDataC">PolygonData</a>
  - <a href="sdk-for-ios-explore-classes-polygondataaccessor">PolygonDataAccessor</a>
  - <a href="sdk-for-ios-explore-classes-polygondatabuilder">PolygonDataBuilder</a>
  - <a href="sdk-for-ios-explore-classes-polygondatasource">PolygonDataSource</a>
  - <a href="sdk-for-ios-explore-classes-polygondatasourcebuilder">PolygonDataSourceBuilder</a>
  - <a href="sdk-for-ios-explore-classes-polygontiledatasource">PolygonTileDataSource</a>
  - <a href="sdk-for-ios-explore-protocols-polygontilesource">PolygonTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-polygontilesourceloadresulthandler">PolygonTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-classes-quadmeshbuilder">QuadMeshBuilder</a>
  - <a href="sdk-for-ios-explore-classes-rasterdatasource">RasterDataSource</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration">RasterDataSourceConfiguration</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-provider">– Provider</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfiguration-cache">– Cache</a>
  - <a href="sdk-for-ios-explore-structs-rasterdatasourceconfigurationupdate">RasterDataSourceConfigurationUpdate</a>
  - <a href="sdk-for-ios-explore-protocols-rasterdatasourcedelegate">RasterDataSourceDelegate</a>
  - <a href="sdk-for-ios-explore-enums-rasterdatasourceerror">RasterDataSourceError</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesource">RasterTileSource</a>
  - <a href="sdk-for-ios-explore-protocols-rastertilesourceloadresulthandler">RasterTileSourceLoadResultHandler</a>
  - <a href="sdk-for-ios-explore-structs-roadshieldiconproperties">RoadShieldIconProperties</a>
  - <a href="sdk-for-ios-explore-structs-rendersize">RenderSize</a>
  - <a href="sdk-for-ios-explore-structs-rendersize-unit">– Unit</a>
  - <a href="sdk-for-ios-explore-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-sdkmapviewinitializer">SDKMapViewInitializer</a>
  - <a href="sdk-for-ios-explore-enums-shadowquality">ShadowQuality</a>
  - <a href="sdk-for-ios-explore-classes-style">Style</a>
  - <a href="sdk-for-ios-explore-protocols-tapdelegate">TapDelegate</a>
  - <a href="sdk-for-ios-explore-classes-tilegeoboundscalculator">TileGeoBoundsCalculator</a>
  - <a href="sdk-for-ios-explore-protocols-tilesource">TileSource</a>
  - <a href="sdk-for-ios-explore-structs-tilesourcedataversion">TileSourceDataVersion</a>
  - <a href="sdk-for-ios-explore-protocols-tilesourcedelegate">TileSourceDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-tilesourceloadtilerequesthandle">TileSourceLoadTileRequestHandle</a>
  - <a href="sdk-for-ios-explore-structs-tilesourcetilemetadata">TileSourceTileMetadata</a>
  - <a href="sdk-for-ios-explore-structs-tilekey">TileKey</a>
  - <a href="sdk-for-ios-explore-classes-tileurlproviderfactory">TileUrlProviderFactory</a>
  - <a href="sdk-for-ios-explore-maps#/s:7heresdk21TileUrlRequestHandlera">TileUrlRequestHandler</a>
  - <a href="sdk-for-ios-explore-enums-tilingscheme">TilingScheme</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup">TranslucentMapLayerGroup</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup-errorcode">– ErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-translucentmaplayergroup-errordetails">– ErrorDetails</a>
  - <a href="sdk-for-ios-explore-classes-trianglemeshbuilder">TriangleMeshBuilder</a>
  - <a href="sdk-for-ios-explore-protocols-twofingerpandelegate">TwoFingerPanDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-twofingertapdelegate">TwoFingerTapDelegate</a>
  - <a href="sdk-for-ios-explore-enums-visibilitystate">VisibilityState</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictioniconproperties">VehicleRestrictionIconProperties</a>
  - <a href="sdk-for-ios-explore-enums-watermarkstyle">WatermarkStyle</a>
- <a href="sdk-for-ios-explore-routing">Routing</a>
  - <a href="sdk-for-ios-explore-enums-accessattributes">AccessAttributes</a>
  - <a href="sdk-for-ios-explore-structs-agency">Agency</a>
  - <a href="sdk-for-ios-explore-structs-allowoptions">AllowOptions</a>
  - <a href="sdk-for-ios-explore-structs-attribution">Attribution</a>
  - <a href="sdk-for-ios-explore-enums-attributiontype">AttributionType</a>
  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidboundingboxareaoptions">AvoidBoundingBoxAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidcorridorareaoptions">AvoidCorridorAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidpolygonareaoptions">AvoidPolygonAreaOptions</a>
  - <a href="sdk-for-ios-explore-structs-batteryspecifications">BatterySpecifications</a>
  - <a href="sdk-for-ios-explore-structs-bicycleoptions">BicycleOptions</a>
  - <a href="sdk-for-ios-explore-structs-busoptions">BusOptions</a>
  - <a href="sdk-for-ios-explore-structs-caroptions">CarOptions</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk37CalculateIndoorRouteCompletionHandlera">CalculateIndoorRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-routing#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-chargingactiondetails">ChargingActionDetails</a>
  - <a href="sdk-for-ios-explore-structs-chargingconnectorattributes">ChargingConnectorAttributes</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype">ChargingConnectorType</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype-key">– Key</a>
  - <a href="sdk-for-ios-explore-enums-chargingconnectortype-codingerror">– CodingError</a>
  - <a href="sdk-for-ios-explore-structs-chargingstation">ChargingStation</a>
  - <a href="sdk-for-ios-explore-structs-chargingstop">ChargingStop</a>
  - <a href="sdk-for-ios-explore-enums-chargingsupplytype">ChargingSupplyType</a>
  - <a href="sdk-for-ios-explore-structs-dynamicspeedinfo">DynamicSpeedInfo</a>
  - <a href="sdk-for-ios-explore-structs-electricvehicleoptions">ElectricVehicleOptions</a>
  - <a href="sdk-for-ios-explore-structs-empiricalconsumptionmodel">EmpiricalConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-evcaroptions">EVCarOptions</a>
  - <a href="sdk-for-ios-explore-structs-evchargingpool">EVChargingPool</a>
  - <a href="sdk-for-ios-explore-structs-evchargingstation">EVChargingStation</a>
  - <a href="sdk-for-ios-explore-structs-evconsumptionmodel">EVConsumptionModel</a>
  - <a href="sdk-for-ios-explore-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a>
  - <a href="sdk-for-ios-explore-structs-evtruckoptions">EVTruckOptions</a>
  - <a href="sdk-for-ios-explore-structs-fare">Fare</a>
  - <a href="sdk-for-ios-explore-structs-farepassvalidityperiod">FarePassValidityPeriod</a>
  - <a href="sdk-for-ios-explore-enums-farepassvalidityperiodtype">FarePassValidityPeriodType</a>
  - <a href="sdk-for-ios-explore-structs-fareprice">FarePrice</a>
  - <a href="sdk-for-ios-explore-enums-farepricetype">FarePriceType</a>
  - <a href="sdk-for-ios-explore-enums-farereason">FareReason</a>
  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterial">HazardousMaterial</a>
  - <a href="sdk-for-ios-explore-structs-indooravoidanceoptions">IndoorAvoidanceOptions</a>
  - <a href="sdk-for-ios-explore-classes-indoormaneuver">IndoorManeuver</a>
  - <a href="sdk-for-ios-explore-structs-indoorrouteoptions">IndoorRouteOptions</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutestyle">IndoorRouteStyle</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutingcontroller">IndoorRoutingController</a>
  - <a href="sdk-for-ios-explore-classes-indoorroutingengine">IndoorRoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-indoorroutingerror">IndoorRoutingError</a>
  - <a href="sdk-for-ios-explore-classes-indoorwaypoint">IndoorWaypoint</a>
  - <a href="sdk-for-ios-explore-classes-isoline">Isoline</a>
  - <a href="sdk-for-ios-explore-enums-isolinecalculationmode">IsolineCalculationMode</a>
  - <a href="sdk-for-ios-explore-structs-isolineoptions">IsolineOptions</a>
  - <a href="sdk-for-ios-explore-structs-isolineoptions-calculation">– Calculation</a>
  - <a href="sdk-for-ios-explore-enums-isolinerangetype">IsolineRangeType</a>
  - <a href="sdk-for-ios-explore-classes-isolineroutingengine">IsolineRoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-localizedtextpreference">LocalizedTextPreference</a>
  - <a href="sdk-for-ios-explore-classes-maneuver">Maneuver</a>
  - <a href="sdk-for-ios-explore-enums-maneuveraction">ManeuverAction</a>
  - <a href="sdk-for-ios-explore-structs-mapdatasize">MapDataSize</a>
  - <a href="sdk-for-ios-explore-protocols-mapdatasizelistener">MapDataSizeListener</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedcoordinates">MapMatchedCoordinates</a>
  - <a href="sdk-for-ios-explore-enums-matchsideofstreet">MatchSideOfStreet</a>
  - <a href="sdk-for-ios-explore-structs-maxaxlegroupweight">MaxAxleGroupWeight</a>
  - <a href="sdk-for-ios-explore-structs-maxspeedonsegment">MaxSpeedOnSegment</a>
  - <a href="sdk-for-ios-explore-enums-noticeseverity">NoticeSeverity</a>
  - <a href="sdk-for-ios-explore-classes-offlineroutingengine">OfflineRoutingEngine</a>
  - <a href="sdk-for-ios-explore-structs-offlineroutingengineoptions">OfflineRoutingEngineOptions</a>
  - <a href="sdk-for-ios-explore-enums-optimizationmode">OptimizationMode</a>
  - <a href="sdk-for-ios-explore-structs-passthroughwaypoint">PassThroughWaypoint</a>
  - <a href="sdk-for-ios-explore-enums-paymentmethod">PaymentMethod</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianoptions">PedestrianOptions</a>
  - <a href="sdk-for-ios-explore-structs-physicalconsumptionmodel">PhysicalConsumptionModel</a>
  - <a href="sdk-for-ios-explore-classes-polygonprefetcher">PolygonPrefetcher</a>
  - <a href="sdk-for-ios-explore-structs-postaction">PostAction</a>
  - <a href="sdk-for-ios-explore-protocols-postactiondelegate">PostActionDelegate</a>
  - <a href="sdk-for-ios-explore-enums-postactiontype">PostActionType</a>
  - <a href="sdk-for-ios-explore-structs-preaction">PreAction</a>
  - <a href="sdk-for-ios-explore-enums-preactiontype">PreActionType</a>
  - <a href="sdk-for-ios-explore-protocols-prefetchstatuslistener">PrefetchStatusListener</a>
  - <a href="sdk-for-ios-explore-structs-privatebusoptions">PrivateBusOptions</a>
  - <a href="sdk-for-ios-explore-classes-refreshrouteoptions">RefreshRouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-roadattributes">RoadAttributes</a>
  - <a href="sdk-for-ios-explore-protocols-roadattributesdelegate">RoadAttributesDelegate</a>
  - <a href="sdk-for-ios-explore-enums-roadfeatures">RoadFeatures</a>
  - <a href="sdk-for-ios-explore-structs-roadtexts">RoadTexts</a>
  - <a href="sdk-for-ios-explore-classes-route">Route</a>
  - <a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a>
  - <a href="sdk-for-ios-explore-structs-routelabel">RouteLabel</a>
  - <a href="sdk-for-ios-explore-enums-routelabeltype">RouteLabelType</a>
  - <a href="sdk-for-ios-explore-structs-routeoffset">RouteOffset</a>
  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-routeplace">RoutePlace</a>
  - <a href="sdk-for-ios-explore-enums-routeplacedirection">RoutePlaceDirection</a>
  - <a href="sdk-for-ios-explore-enums-routeplacetype">RoutePlaceType</a>
  - <a href="sdk-for-ios-explore-classes-routeprefetcher">RoutePrefetcher</a>
  - <a href="sdk-for-ios-explore-structs-routerailwaycrossing">RouteRailwayCrossing</a>
  - <a href="sdk-for-ios-explore-enums-routerailwaycrossingtype">RouteRailwayCrossingType</a>
  - <a href="sdk-for-ios-explore-structs-routestop">RouteStop</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-explore-structs-routingconnectionsettings">RoutingConnectionSettings</a>
  - <a href="sdk-for-ios-explore-classes-routingengine">RoutingEngine</a>
  - <a href="sdk-for-ios-explore-enums-routingerror">RoutingError</a>
  - <a href="sdk-for-ios-explore-structs-routingoptions">RoutingOptions</a>
  - <a href="sdk-for-ios-explore-protocols-routingprotocol">RoutingProtocol</a>
  - <a href="sdk-for-ios-explore-structs-scooteroptions">ScooterOptions</a>
  - <a href="sdk-for-ios-explore-classes-section">Section</a>
  - <a href="sdk-for-ios-explore-structs-sectionnotice">SectionNotice</a>
  - <a href="sdk-for-ios-explore-enums-sectionnoticecode">SectionNoticeCode</a>
  - <a href="sdk-for-ios-explore-enums-sectiontransportmode">SectionTransportMode</a>
  - <a href="sdk-for-ios-explore-structs-segmentreference">SegmentReference</a>
  - <a href="sdk-for-ios-explore-enums-sideofdestination">SideOfDestination</a>
  - <a href="sdk-for-ios-explore-structs-signpost">Signpost</a>
  - <a href="sdk-for-ios-explore-structs-signpostlabel">SignpostLabel</a>
  - <a href="sdk-for-ios-explore-enums-streetattributes">StreetAttributes</a>
  - <a href="sdk-for-ios-explore-classes-span">Span</a>
  - <a href="sdk-for-ios-explore-structs-taxioptions">TaxiOptions</a>
  - <a href="sdk-for-ios-explore-structs-textusageoptions">TextUsageOptions</a>
  - <a href="sdk-for-ios-explore-structs-toll">Toll</a>
  - <a href="sdk-for-ios-explore-structs-tollfare">TollFare</a>
  - <a href="sdk-for-ios-explore-structs-tollfarepass">TollFarePass</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions">TollOptions</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-vehiclecategory">– VehicleCategory</a>
  - <a href="sdk-for-ios-explore-structs-tolloptions-emissiontype">– EmissionType</a>
  - <a href="sdk-for-ios-explore-structs-trafficonroute">TrafficOnRoute</a>
  - <a href="sdk-for-ios-explore-structs-trafficonspan">TrafficOnSpan</a>
  - <a href="sdk-for-ios-explore-structs-trafficonsection">TrafficOnSection</a>
  - <a href="sdk-for-ios-explore-structs-transitdeparture">TransitDeparture</a>
  - <a href="sdk-for-ios-explore-enums-transitdeparturestatus">TransitDepartureStatus</a>
  - <a href="sdk-for-ios-explore-structs-transitincident">TransitIncident</a>
  - <a href="sdk-for-ios-explore-enums-transitincidenteffect">TransitIncidentEffect</a>
  - <a href="sdk-for-ios-explore-enums-transitincidenttype">TransitIncidentType</a>
  - <a href="sdk-for-ios-explore-enums-transitmode">TransitMode</a>
  - <a href="sdk-for-ios-explore-enums-transitmodefilter">TransitModeFilter</a>
  - <a href="sdk-for-ios-explore-enums-trafficoptimizationmode">TrafficOptimizationMode</a>
  - <a href="sdk-for-ios-explore-structs-transitrouteoptions">TransitRouteOptions</a>
  - <a href="sdk-for-ios-explore-classes-transitroutingengine">TransitRoutingEngine</a>
  - <a href="sdk-for-ios-explore-structs-transitsectiondetails">TransitSectionDetails</a>
  - <a href="sdk-for-ios-explore-structs-transitstop">TransitStop</a>
  - <a href="sdk-for-ios-explore-structs-transittransport">TransitTransport</a>
  - <a href="sdk-for-ios-explore-structs-transitwaypoint">TransitWaypoint</a>
  - <a href="sdk-for-ios-explore-enums-traveldirection">TravelDirection</a>
  - <a href="sdk-for-ios-explore-structs-truckoptions">TruckOptions</a>
  - <a href="sdk-for-ios-explore-structs-truckspecifications">TruckSpecifications</a>
  - <a href="sdk-for-ios-explore-enums-trucktype">TruckType</a>
  - <a href="sdk-for-ios-explore-enums-tunnelcategory">TunnelCategory</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a>
  - <a href="sdk-for-ios-explore-enums-vehiclerestrictionmaxweighttype">VehicleRestrictionMaxWeightType</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification">VehicleSpecification</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-carbuilder">– CarBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-truckbuilder">– TruckBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-scooterbuilder">– ScooterBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-taxibuilder">– TaxiBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-busbuilder">– BusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecification-privatebusbuilder">– PrivateBusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-violatedrestriction">ViolatedRestriction</a>
  - <a href="sdk-for-ios-explore-structs-violatedrestriction-details">– Details</a>
  - <a href="sdk-for-ios-explore-enums-walkattributes">WalkAttributes</a>
  - <a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a>
  - <a href="sdk-for-ios-explore-enums-waypointtype">WaypointType</a>
  - <a href="sdk-for-ios-explore-enums-zonecategory">ZoneCategory</a>
- <a href="sdk-for-ios-explore-navigation">Navigation</a>
  - <a href="sdk-for-ios-explore-classes-areacamerabehavior">AreaCameraBehavior</a>
  - <a href="sdk-for-ios-explore-enums-arrivalnotificationoption">ArrivalNotificationOption</a>
  - <a href="sdk-for-ios-explore-enums-aspectratio">AspectRatio</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior">AutomotiveCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior-orientationmode">– OrientationMode</a>
  - <a href="sdk-for-ios-explore-classes-automotivecamerabehavior-activecameratype">– ActiveCameraType</a>
  - <a href="sdk-for-ios-explore-enums-bordercrossingtype">BorderCrossingType</a>
  - <a href="sdk-for-ios-explore-structs-bordercrossingwarning">BorderCrossingWarning</a>
  - <a href="sdk-for-ios-explore-protocols-bordercrossingwarningdelegate">BorderCrossingWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-bordercrossingwarningoptions">BorderCrossingWarningOptions</a>
  - <a href="sdk-for-ios-explore-protocols-camerabehavior">CameraBehavior</a>
  - <a href="sdk-for-ios-explore-structs-currentsituationlaneview">CurrentSituationLaneView</a>
  - <a href="sdk-for-ios-explore-structs-currentsituationlaneassistanceview">CurrentSituationLaneAssistanceView</a>
  - <a href="sdk-for-ios-explore-protocols-currentsituationlaneassistanceviewdelegate">CurrentSituationLaneAssistanceViewDelegate</a>
  - <a href="sdk-for-ios-explore-structs-custompanningdata">CustomPanningData</a>
  - <a href="sdk-for-ios-explore-structs-dangerzonewarning">DangerZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-dangerzonewarningdelegate">DangerZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-destinationreacheddelegate">DestinationReachedDelegate</a>
  - <a href="sdk-for-ios-explore-structs-dimensionrestriction">DimensionRestriction</a>
  - <a href="sdk-for-ios-explore-enums-dimensionrestrictiontype">DimensionRestrictionType</a>
  - <a href="sdk-for-ios-explore-enums-directioninformationusageoption">DirectionInformationUsageOption</a>
  - <a href="sdk-for-ios-explore-enums-distancetype">DistanceType</a>
  - <a href="sdk-for-ios-explore-enums-dividermarker">DividerMarker</a>
  - <a href="sdk-for-ios-explore-classes-dynamiccamerabehavior">DynamicCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-dynamicroutingengine">DynamicRoutingEngine</a>
  - <a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror">– StartError</a>
  - <a href="sdk-for-ios-explore-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a>
  - <a href="sdk-for-ios-explore-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a>
  - <a href="sdk-for-ios-explore-structs-environmentalzonewarning">EnvironmentalZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-environmentalzonewarningdelegate">EnvironmentalZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-eventtext">EventText</a>
  - <a href="sdk-for-ios-explore-protocols-eventtextdelegate">EventTextDelegate</a>
  - <a href="sdk-for-ios-explore-structs-eventtextoptions">EventTextOptions</a>
  - <a href="sdk-for-ios-explore-classes-fixedcamerabehavior">FixedCameraBehavior</a>
  - <a href="sdk-for-ios-explore-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a>
  - <a href="sdk-for-ios-explore-classes-gpxdocument">GPXDocument</a>
  - <a href="sdk-for-ios-explore-structs-gpxoptions">GPXOptions</a>
  - <a href="sdk-for-ios-explore-classes-gpxtrack">GPXTrack</a>
  - <a href="sdk-for-ios-explore-classes-gpxtrackwriter">GPXTrackWriter</a>
  - <a href="sdk-for-ios-explore-protocols-interpolatedlocationdelegate">InterpolatedLocationDelegate</a>
  - <a href="sdk-for-ios-explore-structs-junctionviewlaneassistance">JunctionViewLaneAssistance</a>
  - <a href="sdk-for-ios-explore-protocols-junctionviewlaneassistancedelegate">JunctionViewLaneAssistanceDelegate</a>
  - <a href="sdk-for-ios-explore-structs-lane">Lane</a>
  - <a href="sdk-for-ios-explore-structs-laneaccess">LaneAccess</a>
  - <a href="sdk-for-ios-explore-enums-lanedirection">LaneDirection</a>
  - <a href="sdk-for-ios-explore-structs-lanedirectioncategory">LaneDirectionCategory</a>
  - <a href="sdk-for-ios-explore-structs-lanemarkings">LaneMarkings</a>
  - <a href="sdk-for-ios-explore-enums-lanerecommendationstate">LaneRecommendationState</a>
  - <a href="sdk-for-ios-explore-structs-lanetype">LaneType</a>
  - <a href="sdk-for-ios-explore-structs-lowspeedzonewarning">LowSpeedZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-lowspeedzonewarningdelegate">LowSpeedZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationdetails">ManeuverNotificationDetails</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationoptions">ManeuverNotificationOptions</a>
  - <a href="sdk-for-ios-explore-structs-maneuvernotificationtimingoptions">ManeuverNotificationTimingOptions</a>
  - <a href="sdk-for-ios-explore-enums-maneuvernotificationtype">ManeuverNotificationType</a>
  - <a href="sdk-for-ios-explore-structs-maneuverprogress">ManeuverProgress</a>
  - <a href="sdk-for-ios-explore-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a>
  - <a href="sdk-for-ios-explore-protocols-maneuverviewlaneassistancedelegate">ManeuverViewLaneAssistanceDelegate</a>
  - <a href="sdk-for-ios-explore-structs-mapmatchedlocation">MapMatchedLocation</a>
  - <a href="sdk-for-ios-explore-structs-milestone">Milestone</a>
  - <a href="sdk-for-ios-explore-enums-milestonestatus">MilestoneStatus</a>
  - <a href="sdk-for-ios-explore-protocols-milestonestatusdelegate">MilestoneStatusDelegate</a>
  - <a href="sdk-for-ios-explore-enums-milestonetype">MilestoneType</a>
  - <a href="sdk-for-ios-explore-enums-naturalguidancetype">NaturalGuidanceType</a>
  - <a href="sdk-for-ios-explore-structs-navigablelocation">NavigableLocation</a>
  - <a href="sdk-for-ios-explore-protocols-navigablelocationdelegate">NavigableLocationDelegate</a>
  - <a href="sdk-for-ios-explore-classes-navigator">Navigator</a>
  - <a href="sdk-for-ios-explore-protocols-navigatorprotocol">NavigatorProtocol</a>
  - <a href="sdk-for-ios-explore-enums-notificationformatoption">NotificationFormatOption</a>
  - <a href="sdk-for-ios-explore-protocols-offroaddestinationreacheddelegate">OffRoadDestinationReachedDelegate</a>
  - <a href="sdk-for-ios-explore-structs-offroadprogress">OffRoadProgress</a>
  - <a href="sdk-for-ios-explore-protocols-offroadprogressdelegate">OffRoadProgressDelegate</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewrasterimage">RealisticViewRasterImage</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewvectorimage">RealisticViewVectorImage</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewwarning">RealisticViewWarning</a>
  - <a href="sdk-for-ios-explore-protocols-realisticviewwarningdelegate">RealisticViewWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-realisticviewwarningoptions">RealisticViewWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-railwaycrossingwarning">RailwayCrossingWarning</a>
  - <a href="sdk-for-ios-explore-protocols-railwaycrossingwarningdelegate">RailwayCrossingWarningDelegate</a>
  - <a href="sdk-for-ios-explore-enums-roadclassification">RoadClassification</a>
  - <a href="sdk-for-ios-explore-structs-roadsign">RoadSign</a>
  - <a href="sdk-for-ios-explore-enums-roadsigncategory">RoadSignCategory</a>
  - <a href="sdk-for-ios-explore-enums-roadsigntype">RoadSignType</a>
  - <a href="sdk-for-ios-explore-structs-roadsignwarning">RoadSignWarning</a>
  - <a href="sdk-for-ios-explore-protocols-roadsignwarningdelegate">RoadSignWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-roadsignwarningoptions">RoadSignWarningOptions</a>
  - <a href="sdk-for-ios-explore-enums-roadsignvehicletype">RoadSignVehicleType</a>
  - <a href="sdk-for-ios-explore-protocols-roadtextsdelegate">RoadTextsDelegate</a>
  - <a href="sdk-for-ios-explore-structs-routedeviation">RouteDeviation</a>
  - <a href="sdk-for-ios-explore-protocols-routedeviationdelegate">RouteDeviationDelegate</a>
  - <a href="sdk-for-ios-explore-structs-routematchedlocation">RouteMatchedLocation</a>
  - <a href="sdk-for-ios-explore-structs-routeprogress">RouteProgress</a>
  - <a href="sdk-for-ios-explore-structs-routeprogresscolors">RouteProgressColors</a>
  - <a href="sdk-for-ios-explore-protocols-routeprogressdelegate">RouteProgressDelegate</a>
  - <a href="sdk-for-ios-explore-enums-safetycameratype">SafetyCameraType</a>
  - <a href="sdk-for-ios-explore-structs-safetycamerawarning">SafetyCameraWarning</a>
  - <a href="sdk-for-ios-explore-protocols-safetycamerawarningdelegate">SafetyCameraWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-safetycamerawarningoptions">SafetyCameraWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-schoolzonewarning">SchoolZoneWarning</a>
  - <a href="sdk-for-ios-explore-protocols-schoolzonewarningdelegate">SchoolZoneWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-schoolzonewarningoptions">SchoolZoneWarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-sdknavigationinitializer">SDKNavigationInitializer</a>
  - <a href="sdk-for-ios-explore-structs-sectionprogress">SectionProgress</a>
  - <a href="sdk-for-ios-explore-classes-spatialaudiocuepanning">SpatialAudioCuePanning</a>
  - <a href="sdk-for-ios-explore-structs-spatialnotificationdetails">SpatialNotificationDetails</a>
  - <a href="sdk-for-ios-explore-structs-spatialtrajectorydata">SpatialTrajectoryData</a>
  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior">SpeedBasedCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">– ProfileValue</a>
  - <a href="sdk-for-ios-explore-structs-speedlimit">SpeedLimit</a>
  - <a href="sdk-for-ios-explore-protocols-speedlimitdelegate">SpeedLimitDelegate</a>
  - <a href="sdk-for-ios-explore-structs-speedlimitoffset">SpeedLimitOffset</a>
  - <a href="sdk-for-ios-explore-protocols-speedwarningdelegate">SpeedWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-speedwarningoptions">SpeedWarningOptions</a>
  - <a href="sdk-for-ios-explore-enums-speedwarningstatus">SpeedWarningStatus</a>
  - <a href="sdk-for-ios-explore-enums-textnotificationtype">TextNotificationType</a>
  - <a href="sdk-for-ios-explore-enums-timingprofile">TimingProfile</a>
  - <a href="sdk-for-ios-explore-structs-tollbooth">TollBooth</a>
  - <a href="sdk-for-ios-explore-structs-tollboothlane">TollBoothLane</a>
  - <a href="sdk-for-ios-explore-enums-tollcollectionmethod">TollCollectionMethod</a>
  - <a href="sdk-for-ios-explore-structs-tollstop">TollStop</a>
  - <a href="sdk-for-ios-explore-protocols-tollstopwarningdelegate">TollStopWarningDelegate</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-zoompolicy">– ZoomPolicy</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-speedthreshold">– SpeedThreshold</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">– FunctionalRoadClassZoomPolicyOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">– SpeedBasedZoomPolicyOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverzoomrange">– ManeuverZoomRange</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverruleoptions">– ManeuverRuleOptions</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule">– ManeuverRule</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuvermodeconfiguration">– ManeuverModeConfiguration</a>
  - <a href="sdk-for-ios-explore-enums-trafficmergeroadtype">TrafficMergeRoadType</a>
  - <a href="sdk-for-ios-explore-enums-trafficmergeside">TrafficMergeSide</a>
  - <a href="sdk-for-ios-explore-structs-trafficmergewarning">TrafficMergeWarning</a>
  - <a href="sdk-for-ios-explore-protocols-trafficmergewarningdelegate">TrafficMergeWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-trafficmergewarningoptions">TrafficMergeWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-trafficonroutecolors">TrafficOnRouteColors</a>
  - <a href="sdk-for-ios-explore-structs-truckrestrictionwarning">TruckRestrictionWarning</a>
  - <a href="sdk-for-ios-explore-protocols-truckrestrictionswarningdelegate">TruckRestrictionsWarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-truckrestrictionswarningoptions">TruckRestrictionsWarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-visualnavigator">VisualNavigator</a>
  - <a href="sdk-for-ios-explore-classes-visualnavigatorcolors">VisualNavigatorColors</a>
  - <a href="sdk-for-ios-explore-protocols-wallclock">WallClock</a>
  - <a href="sdk-for-ios-explore-structs-warningnotificationdistances">WarningNotificationDistances</a>
  - <a href="sdk-for-ios-explore-enums-warningtype">WarningType</a>
  - <a href="sdk-for-ios-explore-enums-weathertype">WeatherType</a>
  - <a href="sdk-for-ios-explore-structs-weightrestriction">WeightRestriction</a>
  - <a href="sdk-for-ios-explore-enums-weightrestrictiontype">WeightRestrictionType</a>
- <a href="sdk-for-ios-explore-search">Search</a>
  - <a href="sdk-for-ios-explore-structs-address">Address</a>
  - <a href="sdk-for-ios-explore-enums-addresstype">AddressType</a>
  - <a href="sdk-for-ios-explore-structs-addressquery">AddressQuery</a>
  - <a href="sdk-for-ios-explore-enums-areatype">AreaType</a>
  - <a href="sdk-for-ios-explore-structs-businessdetails">BusinessDetails</a>
  - <a href="sdk-for-ios-explore-structs-categoryquery">CategoryQuery</a>
  - <a href="sdk-for-ios-explore-structs-categoryquery-area">– Area</a>
  - <a href="sdk-for-ios-explore-structs-contact">Contact</a>
  - <a href="sdk-for-ios-explore-structs-daterange">DateRange</a>
  - <a href="sdk-for-ios-explore-enums-dayofweek">DayOfWeek</a>
  - <a href="sdk-for-ios-explore-structs-details">Details</a>
  - <a href="sdk-for-ios-explore-structs-emailaddress">EmailAddress</a>
  - <a href="sdk-for-ios-explore-structs-emobilityserviceprovider">EMobilityServiceProvider</a>
  - <a href="sdk-for-ios-explore-structs-energymix">EnergyMix</a>
  - <a href="sdk-for-ios-explore-structs-energysource">EnergySource</a>
  - <a href="sdk-for-ios-explore-enums-energysourcetype">EnergySourceType</a>
  - <a href="sdk-for-ios-explore-structs-environmentalimpact">EnvironmentalImpact</a>
  - <a href="sdk-for-ios-explore-enums-environmentalimpactcategory">EnvironmentalImpactCategory</a>
  - <a href="sdk-for-ios-explore-enums-evaccessrestrictionreason">EVAccessRestrictionReason</a>
  - <a href="sdk-for-ios-explore-enums-evaccesstype">EVAccessType</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnector">EVChargingConnector</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectorgroup">EVChargingConnectorGroup</a>
  - <a href="sdk-for-ios-explore-structs-evchargingconnectorreference">EVChargingConnectorReference</a>
  - <a href="sdk-for-ios-explore-structs-evchargingdurationrange">EVChargingDurationRange</a>
  - <a href="sdk-for-ios-explore-classes-evcharginglocation">EVChargingLocation</a>
  - <a href="sdk-for-ios-explore-enums-evcharginglocationfeature">EVChargingLocationFeature</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghours">EVChargingOpeningHours</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghoursexception">EVChargingOpeningHoursException</a>
  - <a href="sdk-for-ios-explore-structs-evchargingopeninghoursschedule">EVChargingOpeningHoursSchedule</a>
  - <a href="sdk-for-ios-explore-structs-evchargingoperator">EVChargingOperator</a>
  - <a href="sdk-for-ios-explore-structs-evchargingpooldetails">EVChargingPoolDetails</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariff">EVChargingTariff</a>
  - <a href="sdk-for-ios-explore-enums-evchargingtariffdimension">EVChargingTariffDimension</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelement">EVChargingTariffElement</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffrequest">EVChargingTariffRequest</a>
  - <a href="sdk-for-ios-explore-enums-evchargingtarifftype">EVChargingTariffType</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtruckrestriction">EVChargingTruckRestriction</a>
  - <a href="sdk-for-ios-explore-enums-evchargingvehiclecategory">EVChargingVehicleCategory</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk28EVCP3SearchCompletionHandlera">EVCP3SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-evse">Evse</a>
  - <a href="sdk-for-ios-explore-classes-evsearchengine">EVSearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-evsearcherror">EVSearchError</a>
  - <a href="sdk-for-ios-explore-protocols-evsearchinterface">EVSearchInterface</a>
  - <a href="sdk-for-ios-explore-structs-evsearchoptions">EVSearchOptions</a>
  - <a href="sdk-for-ios-explore-structs-evseconnector">EVSEConnector</a>
  - <a href="sdk-for-ios-explore-structs-evseinfo">EVSEInfo</a>
  - <a href="sdk-for-ios-explore-enums-evsestatus">EVSEStatus</a>
  - <a href="sdk-for-ios-explore-enums-facilitytype">FacilityType</a>
  - <a href="sdk-for-ios-explore-structs-fueladditive">FuelAdditive</a>
  - <a href="sdk-for-ios-explore-enums-fueladditivetype">FuelAdditiveType</a>
  - <a href="sdk-for-ios-explore-structs-fuelstation">FuelStation</a>
  - <a href="sdk-for-ios-explore-enums-fueltype">FuelType</a>
  - <a href="sdk-for-ios-explore-structs-genericfuel">GenericFuel</a>
  - <a href="sdk-for-ios-explore-structs-geoplace">GeoPlace</a>
  - <a href="sdk-for-ios-explore-enums-highlighttype">HighlightType</a>
  - <a href="sdk-for-ios-explore-classes-indexrange">IndexRange</a>
  - <a href="sdk-for-ios-explore-structs-landlinephone">LandlinePhone</a>
  - <a href="sdk-for-ios-explore-structs-locationdetails">LocationDetails</a>
  - <a href="sdk-for-ios-explore-structs-mobilephone">MobilePhone</a>
  - <a href="sdk-for-ios-explore-classes-myplaces">MyPlaces</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchengine">OfflineSearchEngine</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex">OfflineSearchIndex</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-operation">– Operation</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-error">– Error</a>
  - <a href="sdk-for-ios-explore-classes-offlinesearchindex-options">– Options</a>
  - <a href="sdk-for-ios-explore-protocols-offlinesearchindexlistener">OfflineSearchIndexListener</a>
  - <a href="sdk-for-ios-explore-structs-openinghours">OpeningHours</a>
  - <a href="sdk-for-ios-explore-enums-parkingtype">ParkingType</a>
  - <a href="sdk-for-ios-explore-classes-place">Place</a>
  - <a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a>
  - <a href="sdk-for-ios-explore-structs-placechain">PlaceChain</a>
  - <a href="sdk-for-ios-explore-structs-placefilter">PlaceFilter</a>
  - <a href="sdk-for-ios-explore-structs-placefilter-ev">– Ev</a>
  - <a href="sdk-for-ios-explore-structs-placefoodtype">PlaceFoodType</a>
  - <a href="sdk-for-ios-explore-structs-placeidquery">PlaceIdQuery</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk30PlaceIdSearchCompletionHandlera">PlaceIdSearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk38PlaceIdSearchExtendedCompletionHandlera">PlaceIdSearchExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-placeserializationerror">PlaceSerializationError</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk27PlaceSerializationExceptiona">PlaceSerializationException</a>
  - <a href="sdk-for-ios-explore-enums-placetype">PlaceType</a>
  - <a href="sdk-for-ios-explore-structs-poipaymentdetails">POIPaymentDetails</a>
  - <a href="sdk-for-ios-explore-structs-poipaymentmethod">POIPaymentMethod</a>
  - <a href="sdk-for-ios-explore-structs-responsedetails">ResponseDetails</a>
  - <a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk23SearchCompletionHandlera">SearchCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk31SearchExtendedCompletionHandlera">SearchExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-classes-searchengine">SearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-searcherror">SearchError</a>
  - <a href="sdk-for-ios-explore-protocols-searchinterface">SearchInterface</a>
  - <a href="sdk-for-ios-explore-structs-searchoptions">SearchOptions</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery">StructuredQuery</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery-resulttype">– ResultType</a>
  - <a href="sdk-for-ios-explore-structs-structuredquery-addresselements">– AddressElements</a>
  - <a href="sdk-for-ios-explore-classes-suggestion">Suggestion</a>
  - <a href="sdk-for-ios-explore-enums-suggestiontype">SuggestionType</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk24SuggestCompletionHandlera">SuggestCompletionHandler</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk32SuggestExtendedCompletionHandlera">SuggestExtendedCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-supplierreference">SupplierReference</a>
  - <a href="sdk-for-ios-explore-structs-textquery">TextQuery</a>
  - <a href="sdk-for-ios-explore-structs-textquery-area">– Area</a>
  - <a href="sdk-for-ios-explore-structs-timeofdayrange">TimeOfDayRange</a>
  - <a href="sdk-for-ios-explore-structs-truckamenities">TruckAmenities</a>
  - <a href="sdk-for-ios-explore-structs-truckfuel">TruckFuel</a>
  - <a href="sdk-for-ios-explore-structs-webdetails">WebDetails</a>
  - <a href="sdk-for-ios-explore-structs-webeditorial">WebEditorial</a>
  - <a href="sdk-for-ios-explore-structs-webimage">WebImage</a>
  - <a href="sdk-for-ios-explore-structs-webrating">WebRating</a>
  - <a href="sdk-for-ios-explore-structs-websiteaddress">WebsiteAddress</a>
  - <a href="sdk-for-ios-explore-structs-websource">WebSource</a>
  - <a href="sdk-for-ios-explore-classes-w3wsearchengine">W3WSearchEngine</a>
  - <a href="sdk-for-ios-explore-enums-w3wsearcherror">W3WSearchError</a>
  - <a href="sdk-for-ios-explore-structs-w3wsquare">W3WSquare</a>
  - <a href="sdk-for-ios-explore-search#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a>
- <a href="sdk-for-ios-explore-traffic">Traffic</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a>
  - <a href="sdk-for-ios-explore-classes-trafficengine">TrafficEngine</a>
  - <a href="sdk-for-ios-explore-classes-trafficflow">TrafficFlow</a>
  - <a href="sdk-for-ios-explore-protocols-trafficflowbase">TrafficFlowBase</a>
  - <a href="sdk-for-ios-explore-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident">TrafficIncident</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident-restrictedvehiclecategory">– RestrictedVehicleCategory</a>
  - <a href="sdk-for-ios-explore-classes-trafficincident-vehiclerestriction">– VehicleRestriction</a>
  - <a href="sdk-for-ios-explore-protocols-trafficincidentbase">TrafficIncidentBase</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
  - <a href="sdk-for-ios-explore-enums-trafficincidentimpact">TrafficIncidentImpact</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a>
  - <a href="sdk-for-ios-explore-classes-trafficincidentonroute">TrafficIncidentOnRoute</a>
  - <a href="sdk-for-ios-explore-enums-trafficincidenttype">TrafficIncidentType</a>
  - <a href="sdk-for-ios-explore-traffic#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
  - <a href="sdk-for-ios-explore-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a>
  - <a href="sdk-for-ios-explore-structs-trafficlocation">TrafficLocation</a>
  - <a href="sdk-for-ios-explore-enums-trafficqueryerror">TrafficQueryError</a>
  - <a href="sdk-for-ios-explore-enums-traversability">Traversability</a>
- <a href="sdk-for-ios-explore-trafficradio">TrafficRadio</a>
  - <a href="sdk-for-ios-explore-classes-trafficbroadcast">TrafficBroadcast</a>
  - <a href="sdk-for-ios-explore-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a>
  - <a href="sdk-for-ios-explore-structs-tmcdata">TMCData</a>
  - <a href="sdk-for-ios-explore-structs-tmcpreferredsidsrequest">TMCPreferredSidsRequest</a>
  - <a href="sdk-for-ios-explore-structs-tmcserviceproviderinfo">TMCServiceProviderInfo</a>
  - <a href="sdk-for-ios-explore-structs-tmcservicerequest">TMCServiceRequest</a>
  - <a href="sdk-for-ios-explore-protocols-tmcserviceinterface">TMCServiceInterface</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkey">RDSEncryptionKey</a>
  - <a href="sdk-for-ios-explore-structs-rdsencryptionkeysrequest">RDSEncryptionKeysRequest</a>
- <a href="sdk-for-ios-explore-transport">Transport</a>
  - <a href="sdk-for-ios-explore-structs-busspecifications">BusSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-carspecifications">CarSpecifications</a>
  - <a href="sdk-for-ios-explore-structs-generalvehiclespeedlimits">GeneralVehicleSpeedLimits</a>
  - <a href="sdk-for-ios-explore-structs-hazardousmaterialrestriction">HazardousMaterialRestriction</a>
  - <a href="sdk-for-ios-explore-structs-pedestrianspecification">PedestrianSpecification</a>
  - <a href="sdk-for-ios-explore-enums-restrictiontype">RestrictionType</a>
  - <a href="sdk-for-ios-explore-structs-scooterspecification">ScooterSpecification</a>
  - <a href="sdk-for-ios-explore-structs-specificrestriction">SpecificRestriction</a>
  - <a href="sdk-for-ios-explore-structs-taxispecification">TaxiSpecification</a>
  - <a href="sdk-for-ios-explore-structs-timerestriction">TimeRestriction</a>
  - <a href="sdk-for-ios-explore-structs-timerestriction-category">– Category</a>
  - <a href="sdk-for-ios-explore-enums-transportmode">TransportMode</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification">TransportSpecification</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-carbuilder">– CarBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-truckbuilder">– TruckBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-pedestrianbuilder">– PedestrianBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-scooterbuilder">– ScooterBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-bicyclebuilder">– BicycleBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-taxibuilder">– TaxiBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-busbuilder">– BusBuilder</a>
  - <a href="sdk-for-ios-explore-structs-transportspecification-privatebusbuilder">– PrivateBusBuilder</a>
  - <a href="sdk-for-ios-explore-enums-transporttype">TransportType</a>
  - <a href="sdk-for-ios-explore-enums-truckcategory">TruckCategory</a>
  - <a href="sdk-for-ios-explore-enums-truckclass">TruckClass</a>
  - <a href="sdk-for-ios-explore-enums-truckroadtype">TruckRoadType</a>
  - <a href="sdk-for-ios-explore-enums-truckfueltype">TruckFuelType</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestriction">VehicleRestriction</a>
  - <a href="sdk-for-ios-explore-enums-vehicletype">VehicleType</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofile">VehicleProfile</a>
  - <a href="sdk-for-ios-explore-structs-weightperaxlegroup">WeightPerAxleGroup</a>
- <a href="sdk-for-ios-explore-venues">Venues</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk">Crosswalk</a>
  - <a href="sdk-for-ios-explore-classes-crosswalk-classificationstyle">– ClassificationStyle</a>
  - <a href="sdk-for-ios-explore-classes-property">Property</a>
  - <a href="sdk-for-ios-explore-classes-property-propertytype">– PropertyType</a>
  - <a href="sdk-for-ios-explore-classes-venue">Venue</a>
  - <a href="sdk-for-ios-explore-protocols-venuedelegate">VenueDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuedrawing">VenueDrawing</a>
  - <a href="sdk-for-ios-explore-protocols-venuedrawingselectiondelegate">VenueDrawingSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venueengine">VenueEngine</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk10VenueErrora">VenueError</a>
  - <a href="sdk-for-ios-explore-enums-venueerrorcode">VenueErrorCode</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry">VenueGeometry</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-internaladdress">– InternalAddress</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-geometrytype">– GeometryType</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometry-lookuptype">– LookupType</a>
  - <a href="sdk-for-ios-explore-enums-venuegeometryfiltertype">VenueGeometryFilterType</a>
  - <a href="sdk-for-ios-explore-classes-venuegeometrystyle">VenueGeometryStyle</a>
  - <a href="sdk-for-ios-explore-classes-venueinfo">VenueInfo</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk17VenueInfoDataLista">VenueInfoDataList</a>
  - <a href="sdk-for-ios-explore-protocols-venueinfolistlistenerdelegate">VenueInfoListListenerDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuelabelstyle">VenueLabelStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuelevel">VenueLevel</a>
  - <a href="sdk-for-ios-explore-protocols-venuelevelselectiondelegate">VenueLevelSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-venuelifecycledelegate">VenueLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-venues#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>
  - <a href="sdk-for-ios-explore-classes-venuemap">VenueMap</a>
  - <a href="sdk-for-ios-explore-protocols-venuemapdelegate">VenueMapDelegate</a>
  - <a href="sdk-for-ios-explore-protocols-venuemaplifecycledelegate">VenueMapLifecycleDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venuemodel">VenueModel</a>
  - <a href="sdk-for-ios-explore-protocols-venueselectiondelegate">VenueSelectionDelegate</a>
  - <a href="sdk-for-ios-explore-classes-venueservice">VenueService</a>
  - <a href="sdk-for-ios-explore-classes-venueservice-venueoptionalfeature">– VenueOptionalFeature</a>
  - <a href="sdk-for-ios-explore-protocols-venueservicedelegate">VenueServiceDelegate</a>
  - <a href="sdk-for-ios-explore-enums-venueserviceinitstatus">VenueServiceInitStatus</a>
  - <a href="sdk-for-ios-explore-classes-venuestyle">VenueStyle</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology">VenueTopology</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology-accesscharacteristics">– AccessCharacteristics</a>
  - <a href="sdk-for-ios-explore-classes-venuetopology-topologydirectionality">– TopologyDirectionality</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode">VenueTransportMode</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode-key">– Key</a>
  - <a href="sdk-for-ios-explore-enums-venuetransportmode-codingerror">– CodingError</a>
- <a href="sdk-for-ios-explore-warnerengine">WarnerEngine</a>
  - <a href="sdk-for-ios-explore-structs-customwarning">CustomWarning</a>
  - <a href="sdk-for-ios-explore-protocols-customwarningprovider">CustomWarningProvider</a>
  - <a href="sdk-for-ios-explore-structs-warning">Warning</a>
  - <a href="sdk-for-ios-explore-classes-warnerengine">WarnerEngine</a>
  - <a href="sdk-for-ios-explore-protocols-warningdelegate">WarningDelegate</a>
  - <a href="sdk-for-ios-explore-structs-warningoptions">WarningOptions</a>
  - <a href="sdk-for-ios-explore-classes-warningsregistry">WarningsRegistry</a>
- <a href="sdk-for-ios-explore-other%20classes">Other Classes</a>
  - <a href="sdk-for-ios-explore-classes-indoorsectiondetails">IndoorSectionDetails</a>
  - <a href="sdk-for-ios-explore-classes-locationmanager">LocationManager</a>
- <a href="sdk-for-ios-explore-other%20enums">Other Enumerations</a>
  - <a href="sdk-for-ios-explore-enums-commercialvehicleroadtype">CommercialVehicleRoadType</a>
  - <a href="sdk-for-ios-explore-enums-hazardousmaterialtype">HazardousMaterialType</a>
  - <a href="sdk-for-ios-explore-enums-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a>
  - <a href="sdk-for-ios-explore-enums-indoormaneuveractions">IndoorManeuverActions</a>
  - <a href="sdk-for-ios-explore-enums-physicalstructure">PhysicalStructure</a>
  - <a href="sdk-for-ios-explore-enums-vehicletypecondition">VehicleTypeCondition</a>
- <a href="sdk-for-ios-explore-other%20functions">Other Functions</a>
  - <a href="sdk-for-ios-explore-other%20functions#/s:7heresdk24makeIOSPlatformThreadingAA08PlatformD0_pyF">makeIOSPlatformThreading()</a>
  - <a href="sdk-for-ios-explore-other%20functions#/s:7heresdk12synchronized_7closurexyp_xyXEtlF">synchronized(\_:closure:)</a>
- <a href="sdk-for-ios-explore-other%20protocols">Other Protocols</a>
  - <a href="sdk-for-ios-explore-protocols-matchedlocationlistener">MatchedLocationListener</a>
- <a href="sdk-for-ios-explore-other%20structs">Other Structures</a>
  - <a href="sdk-for-ios-explore-structs-admincontextid">AdminContextId</a>
  - <a href="sdk-for-ios-explore-structs-administrativecommercialvehiclerules">AdministrativeCommercialVehicleRules</a>
  - <a href="sdk-for-ios-explore-structs-driverestregulation">DriveRestRegulation</a>
  - <a href="sdk-for-ios-explore-structs-indoorlevelchangedata">IndoorLevelChangeData</a>
  - <a href="sdk-for-ios-explore-structs-indoorrouteplace">IndoorRoutePlace</a>
  - <a href="sdk-for-ios-explore-structs-indoorspacedata">IndoorSpaceData</a>
  - <a href="sdk-for-ios-explore-structs-lanedecreasewarning">LaneDecreaseWarning</a>
  - <a href="sdk-for-ios-explore-structs-lanedecreasewarningoptions">LaneDecreaseWarningOptions</a>
  - <a href="sdk-for-ios-explore-structs-refreshrouteparameters">RefreshRouteParameters</a>
  - <a href="sdk-for-ios-explore-structs-roadprofilecondition">RoadProfileCondition</a>
  - <a href="sdk-for-ios-explore-structs-vehicleprofilerestriction">VehicleProfileRestriction</a>
  - <a href="sdk-for-ios-explore-structs-vehiclerestrictioncondition">VehicleRestrictionCondition</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificaccess">VehicleSpecificAccess</a>
  - <a href="sdk-for-ios-explore-structs-vehiclespecificspeedlimit">VehicleSpecificSpeedLimit</a>

</nav>

<article class="main-content">

<div class="section">

<div class="section section">

# MapLoader

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17CatalogUpdateInfoV"></span>` `<span id="//apple_ref/swift/Struct/CatalogUpdateInfo" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk17CatalogUpdateInfoV" class="token"><code>CatalogUpdateInfo</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Holds information for the catalog update intent. Provides information regarding installed catalog and its latest available version.

  <a href="sdk-for-ios-explore-structs-catalogupdateinfo" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CatalogUpdateInfo : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26CatalogsUpdateInfoCallbacka"></span>` `<span id="//apple_ref/swift/Alias/CatalogsUpdateInfoCallback" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk26CatalogsUpdateInfoCallbacka" class="token"><code>CatalogsUpdateInfoCallback</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when

      MapUpdater.retrieveCatalogsUpdateInfo(...)

  has been completed. The first parameter indicates an error in case of a failure. The second parameter contains the results. Both parameters cannot be `nil` at the same time - or not `nil` at the same time. An empty <a href="sdk-for-ios-explore-structs-catalogupdateinfo">`CatalogUpdateInfo`</a> list represent no map updates.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias CatalogsUpdateInfoCallback = ( _ error : MapLoaderError ?, _ catalogs : [ CatalogUpdateInfo ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>catalogs</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of all catalogs that can be updated. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29CatalogUpdateProgressListenerP"></span>` `<span id="//apple_ref/swift/Protocol/CatalogUpdateProgressListener" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk29CatalogUpdateProgressListenerP" class="token"><code>CatalogUpdateProgressListener</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get notified on status updates when updating catalog, previously downloaded by <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a>.

  <a href="sdk-for-ios-explore-protocols-catalogupdateprogresslistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CatalogUpdateProgressListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18CatalogUpdateStateO"></span>` `<span id="//apple_ref/swift/Enum/CatalogUpdateState" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk18CatalogUpdateStateO" class="token"><code>CatalogUpdateState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the state of catalog map updates.

  <a href="sdk-for-ios-explore-enums-catalogupdatestate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum CatalogUpdateState : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk28ClientCertificateRequestTypeO"></span>` `<span id="//apple_ref/swift/Enum/ClientCertificateRequestType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk28ClientCertificateRequestTypeO" class="token"><code>ClientCertificateRequestType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls the client certificate verification policy on the server.

  <a href="sdk-for-ios-explore-enums-clientcertificaterequesttype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ClientCertificateRequestType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17CompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/CompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk17CompletionHandlera" class="token"><code>CompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler)

  has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias CompletionHandler = ( _ maploaderError : MapLoaderError ?, _ regions : [ Region ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>maploaderError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>regions</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of downloadable regions. It is <code>nil</code> in case of an error. Each region can contain child regions that can contain child regions and so on. Usually, the top-level regions represent continents that contain countries as children.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25ConfigureConnectionHandlea"></span>` `<span id="//apple_ref/swift/Alias/ConfigureConnectionHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk25ConfigureConnectionHandlea" class="token"><code>ConfigureConnectionHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when

      ExternalMapDataSourceClient.configureRemoteConnectionAsync(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias ConfigureConnectionHandle = ( _ errorCode : ExternalMapDataSourceErrorCode ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>errorCode</code></em><code> </code></td>
  <td><div>
  <p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18DataAttributesBaseP"></span>` `<span id="//apple_ref/swift/Protocol/DataAttributesBase" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk18DataAttributesBaseP" class="token"><code>DataAttributesBase</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Interface for a collection of data attributes.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-protocols-dataattributesbase" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DataAttributesBase : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30DeleteRegionsCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/DeleteRegionsCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk30DeleteRegionsCompletionHandlera" class="token"><code>DeleteRegionsCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.deleteRegions(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias DeleteRegionsCompletionHandler = ( _ maploaderError : MapLoaderError ?, _ regions : [ RegionId ]?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>maploaderError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is [null] for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>regions</code></em><code> </code></td>
  <td><div>
  <p>Represents a list of successfully removed map regions. It is [null] in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29DownloadRegionsStatusListenerP"></span>` `<span id="//apple_ref/swift/Protocol/DownloadRegionsStatusListener" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk29DownloadRegionsStatusListenerP" class="token"><code>DownloadRegionsStatusListener</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get notified on status updates when downloading map regions.

  <a href="sdk-for-ios-explore-protocols-downloadregionsstatuslistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol DownloadRegionsStatusListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ExternalMapDataSourceClientC"></span>` `<span id="//apple_ref/swift/Class/ExternalMapDataSourceClient" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk27ExternalMapDataSourceClientC" class="token"><code>ExternalMapDataSourceClient</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-externalmapdatasourceclient" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class ExternalMapDataSourceClient
  ```

  ``` highlight
  extension ExternalMapDataSourceClient: NativeBase
  ```

  ``` highlight
  extension ExternalMapDataSourceClient: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/ExternalMapDataSourceErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk30ExternalMapDataSourceErrorCodeO" class="token"><code>ExternalMapDataSourceErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the reason for failing to configure <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> with external map data source. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-enums-externalmapdatasourceerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ExternalMapDataSourceErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension ExternalMapDataSourceErrorCode : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk35ExternalMapDataSourceExceptionErrora"></span>` `<span id="//apple_ref/swift/Alias/ExternalMapDataSourceExceptionError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk35ExternalMapDataSourceExceptionErrora" class="token"><code>ExternalMapDataSourceExceptionError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias ExternalMapDataSourceExceptionError = ExternalMapDataSourceErrorCode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27ExternalMapDataSourceServerC"></span>` `<span id="//apple_ref/swift/Class/ExternalMapDataSourceServer" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk27ExternalMapDataSourceServerC" class="token"><code>ExternalMapDataSourceServer</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-externalmapdatasourceserver" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class ExternalMapDataSourceServer
  ```

  ``` highlight
  extension ExternalMapDataSourceServer: NativeBase
  ```

  ``` highlight
  extension ExternalMapDataSourceServer: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16InstalledCatalogV"></span>` `<span id="//apple_ref/swift/Struct/InstalledCatalog" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk16InstalledCatalogV" class="token"><code>InstalledCatalog</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents installed catalog.

  <a href="sdk-for-ios-explore-structs-installedcatalog" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstalledCatalog : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15InstalledRegionV"></span>` `<span id="//apple_ref/swift/Struct/InstalledRegion" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk15InstalledRegionV" class="token"><code>InstalledRegion</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a region, from persistent map storage.

  <a href="sdk-for-ios-explore-structs-installedregion" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstalledRegion : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21InstalledRegionStatusO"></span>` `<span id="//apple_ref/swift/Enum/InstalledRegionStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk21InstalledRegionStatusO" class="token"><code>InstalledRegionStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents download status of region in the persistent map storage.

  <a href="sdk-for-ios-explore-enums-installedregionstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstalledRegionStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8LineDataC"></span>` `<span id="//apple_ref/swift/Class/LineData" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC" class="token"><code>LineData</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a geodetic line with custom attributes. Can be created using a <a href="sdk-for-ios-explore-classes-linedatabuilder">`LineDataBuilder`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineData
  ```

  ``` highlight
  extension LineData: NativeBase
  ```

  ``` highlight
  extension LineData: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16LineDataAccessorC"></span>` `<span id="//apple_ref/swift/Class/LineDataAccessor" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk16LineDataAccessorC" class="token"><code>LineDataAccessor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Line data accessor used for manipulating polylines that are part of a LineDataSource.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-linedataaccessor" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataAccessor
  ```

  ``` highlight
  extension LineDataAccessor: NativeBase
  ```

  ``` highlight
  extension LineDataAccessor: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk15LineDataBuilderC"></span>` `<span id="//apple_ref/swift/Class/LineDataBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk15LineDataBuilderC" class="token"><code>LineDataBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of <a href="sdk-for-ios-explore-maploader#/s:7heresdk8LineDataC">`LineData`</a> instances.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-linedatabuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataBuilder
  ```

  ``` highlight
  extension LineDataBuilder: NativeBase
  ```

  ``` highlight
  extension LineDataBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14LineDataSourceC"></span>` `<span id="//apple_ref/swift/Class/LineDataSource" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk14LineDataSourceC" class="token"><code>LineDataSource</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.

  Polyline segments are rendered following the shortest path between their end vertices.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-linedatasource" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataSource
  ```

  ``` highlight
  extension LineDataSource: NativeBase
  ```

  ``` highlight
  extension LineDataSource: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk21LineDataSourceBuilderC"></span>` `<span id="//apple_ref/swift/Class/LineDataSourceBuilder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk21LineDataSourceBuilderC" class="token"><code>LineDataSourceBuilder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builder of lines data source.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-linedatasourcebuilder" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class LineDataSourceBuilder
  ```

  ``` highlight
  extension LineDataSourceBuilder: NativeBase
  ```

  ``` highlight
  extension LineDataSourceBuilder: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14MapLoaderErrorO"></span>` `<span id="//apple_ref/swift/Enum/MapLoaderError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk14MapLoaderErrorO" class="token"><code>MapLoaderError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may result from map downloading/prefetching.

  <a href="sdk-for-ios-explore-enums-maploadererror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapLoaderError : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapLoaderError : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13MapDownloaderC"></span>` `<span id="//apple_ref/swift/Class/MapDownloader" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk13MapDownloaderC" class="token"><code>MapDownloader</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class for downloading and managing map data for various regions worldwide. Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using

      MapDownloader.fromEngineAsync(...)

  .
  </p>

  The storage path for downloaded maps can be specified via <a href="sdk-for-ios-explore-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>.

  To control the type of content included in a map download, use <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a>. Once applied, it affects both the map cache and offline maps. Satellite-based map schemes are not included in the downloaded region data.

  **Note:** During turn-by-turn navigation, while a map download or update is in progress, navigation may not function as expected, and the app may be blocked until the operation is completed. Ensure that all pending map operations are finished before starting navigation. This applies only to `MapDownloader` and <a href="sdk-for-ios-explore-classes-mapupdater">`MapUpdater`</a>. <a href="sdk-for-ios-explore-classes-routeprefetcher">`RoutePrefetcher`</a> operations are not affected.

  <a href="sdk-for-ios-explore-classes-mapdownloader" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapDownloader
  ```

  ``` highlight
  extension MapDownloader: NativeBase
  ```

  ``` highlight
  extension MapDownloader: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk31MapDownloaderConstructionHandlea"></span>` `<span id="//apple_ref/swift/Alias/MapDownloaderConstructionHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk31MapDownloaderConstructionHandlea" class="token"><code>MapDownloaderConstructionHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.fromEngineAsync(...)

  has been completed. The <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> instance is created on a background thread to not block the calling thread.
  </p>

  During construction an online connection is established to fetch configuration data for internal use. If no online connection is available, cached or default values will be used. This is only for internal reasons and has no effect on the operability of the resulting instance. When configuration data is available from the cache, construction can still take a reasonable amount of time. Applications should consider to show a loading indicator.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapDownloaderConstructionHandle = ( _ mapDownloader : MapDownloader ) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapDownloader</code></em><code> </code></td>
  <td><div>
  <p>Represents a constructed MapDownloader object.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18MapLoaderExceptiona"></span>` `<span id="//apple_ref/swift/Alias/MapLoaderException" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk18MapLoaderExceptiona" class="token"><code>MapLoaderException</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error occurred during map operation. `sdk.maploader.MapLoaderError` represents possible errors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapLoaderException = MapLoaderError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17MapDownloaderTaskC"></span>` `<span id="//apple_ref/swift/Class/MapDownloaderTask" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk17MapDownloaderTaskC" class="token"><code>MapDownloaderTask</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to control map download process.

  <a href="sdk-for-ios-explore-classes-mapdownloadertask" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapDownloaderTask
  ```

  ``` highlight
  extension MapDownloaderTask: NativeBase
  ```

  ``` highlight
  extension MapDownloaderTask: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25MapUpdateProgressListenerP"></span>` `<span id="//apple_ref/swift/Protocol/MapUpdateProgressListener" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk25MapUpdateProgressListenerP" class="token"><code>MapUpdateProgressListener</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protocol to get notified on status updates when updating map data, previously downloaded by <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a>.

  <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol MapUpdateProgressListener : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapUpdaterC"></span>` `<span id="//apple_ref/swift/Class/MapUpdater" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk10MapUpdaterC" class="token"><code>MapUpdater</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class for updating regions previously downloaded using the <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a>. First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call

      MapUpdater.retrieveCatalogsUpdateInfo(...)

  to check for available updates for any downloaded regions.
  </p>

  If updates are available, regions can be updated asynchronously using

      MapUpdater.updateCatalog(...)

  . The <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">`MapUpdateProgressListener`</a> provides update progress for each region.
  </p>

  Incremental map updates are supported, by default: Instead of downloading an entire region, only the parts that have changed will be installed. This results in a faster update process. MapUpdater also aligns previously downloaded content with <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> changes made via <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a>.

  Note that patching (also called “incremental updates”) is only supported for up to 8 versions. For example, if an update started with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9. Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.

  In case of an error, the previous map data remains available for use. It is only replaced after new map data has been successfully downloaded. Regions that fail to update must be retried in a new call. Paused updates can be resumed later.

  During the update process, `MapUpdater` internally retries failed downloads until a timeout occurs. If this happens, it is reported via <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">`MapUpdateProgressListener`</a>.

  If the user cancels the update process during the update phase, it is ignored. The update phase begins after all content has been downloaded, then the HERE SDK installs and replaces the existing regions. Cancellation is only possible during the download phase, and a successful cancellation is indicated via

      onComplete(...)

  .
  </p>

  Note that a <a href="sdk-for-ios-explore-enums-maploadererror#/s:7heresdk14MapLoaderErrorO8notReadyyA2CmF">`MapLoaderError.notReady`</a> occurs when the <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> is used in parallel. In general, background updates are not supported explicitly, as the OS can abort background processes. In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is in progress and it will be indicated by a <a href="sdk-for-ios-explore-enums-maploadererror">`MapLoaderError`</a>.

  <a href="sdk-for-ios-explore-classes-mapupdater" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapUpdater
  ```

  ``` highlight
  extension MapUpdater: NativeBase
  ```

  ``` highlight
  extension MapUpdater: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk29MapUpdaterConstructionHandlera"></span>` `<span id="//apple_ref/swift/Alias/MapUpdaterConstructionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk29MapUpdaterConstructionHandlera" class="token"><code>MapUpdaterConstructionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapUpdater.fromEngineAsync(...)

  has been completed. Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread. When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias MapUpdaterConstructionHandler = ( _ mapUpdater : MapUpdater ) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapUpdater</code></em><code> </code></td>
  <td><div>
  <p>Represents a constructed <a href="sdk-for-ios-explore-classes-mapupdater"><code>MapUpdater</code></a> object.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13MapUpdateTaskC"></span>` `<span id="//apple_ref/swift/Class/MapUpdateTask" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk13MapUpdateTaskC" class="token"><code>MapUpdateTask</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class to control the map update process.

  <a href="sdk-for-ios-explore-classes-mapupdatetask" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapUpdateTask
  ```

  ``` highlight
  extension MapUpdateTask: NativeBase
  ```

  ``` highlight
  extension MapUpdateTask: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16MapVersionHandleC"></span>` `<span id="//apple_ref/swift/Class/MapVersionHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk16MapVersionHandleC" class="token"><code>MapVersionHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents version of the map.

  <a href="sdk-for-ios-explore-classes-mapversionhandle" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class MapVersionHandle
  ```

  ``` highlight
  extension MapVersionHandle: NativeBase
  ```

  ``` highlight
  extension MapVersionHandle: Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16NavigabilityTypeO"></span>` `<span id="//apple_ref/swift/Enum/NavigabilityType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk16NavigabilityTypeO" class="token"><code>NavigabilityType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the navigability level of a map region. This enum defines whether a region can be used for navigation purposes. It helps categorize regions based on their usability in routing and map operations.

  <a href="sdk-for-ios-explore-enums-navigabilitytype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum NavigabilityType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk25OfflineStorageSizeHandlera"></span>` `<span id="//apple_ref/swift/Alias/OfflineStorageSizeHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk25OfflineStorageSizeHandlera" class="token"><code>OfflineStorageSizeHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.getOfflineMapsStorageSizeInBytes(OfflineStorageSizeHandler)

  has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias OfflineStorageSizeHandler = ( _ error : MapLoaderError ?, _ size : UInt64 ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>size</code></em><code> </code></td>
  <td><div>
  <p>The size of offline map. It is <code>nil</code> in case of an error.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23RepairCompletionHandlera"></span>` `<span id="//apple_ref/swift/Alias/RepairCompletionHandler" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk23RepairCompletionHandlera" class="token"><code>RepairCompletionHandler</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A method which is called on the main thread when

      MapDownloader.repairPersistentMap(...)

  has been completed. The first argument indicates an error in case of a failure. The second argument contains the results. Both arguments cannot be `nil` at the same time - or not `nil` at the same time.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias RepairCompletionHandler = ( _ persistentMapRepairError : PersistentMapRepairError ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>persistentMapRepairError</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk14PemKeyCertPairV"></span>` `<span id="//apple_ref/swift/Struct/PemKeyCertPair" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk14PemKeyCertPairV" class="token"><code>PemKeyCertPair</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The structure below exactly match the corresponding gRPC PemKeyCertPair structure. A key/certificate pair in PEM format.

  <a href="sdk-for-ios-explore-structs-pemkeycertpair" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct PemKeyCertPair
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24PersistentMapRepairErrorO"></span>` `<span id="//apple_ref/swift/Enum/PersistentMapRepairError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk24PersistentMapRepairErrorO" class="token"><code>PersistentMapRepairError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible errors that may result after a map repair operation has been completed.

  <a href="sdk-for-ios-explore-enums-persistentmaprepairerror" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PersistentMapRepairError : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO"></span>` `<span id="//apple_ref/swift/Enum/PersistentMapStatus" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk19PersistentMapStatusO" class="token"><code>PersistentMapStatus</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies possible statuses of the already downloaded map regions as a whole. Note: This can be valid only for a single region in case of a <a href="sdk-for-ios-explore-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF">`PersistentMapStatus.corrupted`</a> state.

  <a href="sdk-for-ios-explore-enums-persistentmapstatus" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum PersistentMapStatus : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk6RegionV"></span>` `<span id="//apple_ref/swift/Struct/Region" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk6RegionV" class="token"><code>Region</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines an area, especially part of a country or the world that can be downloaded.

  <a href="sdk-for-ios-explore-structs-region" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Region : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk8RegionIdV"></span>` `<span id="//apple_ref/swift/Struct/RegionId" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk8RegionIdV" class="token"><code>RegionId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specify a unique identifier for Region.

  <a href="sdk-for-ios-explore-structs-regionid" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct RegionId : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19ServerStartedHandlea"></span>` `<span id="//apple_ref/swift/Alias/ServerStartedHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk19ServerStartedHandlea" class="token"><code>ServerStartedHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This method will be called on the main thread when

      ExternalMapDataSourceServer.start(...)

  has been completed.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias ServerStartedHandle = ( _ errorCode : ExternalMapDataSourceErrorCode ?) -> Void
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>errorCode</code></em><code> </code></td>
  <td><div>
  <p>Represents the operation status. It is ‘null’ for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27SslClientCredentialsOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SslClientCredentialsOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk27SslClientCredentialsOptionsV" class="token"><code>SslClientCredentialsOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The structure below exactly match the corresponding gRPC SslCredentialsOptions structure. Options used to build SslCredentials.

  <a href="sdk-for-ios-explore-structs-sslclientcredentialsoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SslClientCredentialsOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk27SslServerCredentialsOptionsV"></span>` `<span id="//apple_ref/swift/Struct/SslServerCredentialsOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk27SslServerCredentialsOptionsV" class="token"><code>SslServerCredentialsOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure. Options for configuring a gRPC server with SSL/TLS credentials.

  <a href="sdk-for-ios-explore-structs-sslservercredentialsoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct SslServerCredentialsOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16UpdateStatisticsV"></span>` `<span id="//apple_ref/swift/Struct/UpdateStatistics" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-maploader#/s:7heresdk16UpdateStatisticsV" class="token"><code>UpdateStatistics</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines statistics related to the success or failure of patched bundles. It can be used to monitor and analyze the reliability of binary patch updates.

  <a href="sdk-for-ios-explore-structs-updatestatistics" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct UpdateStatistics
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 <a href="sdk-for-ios-explore" class="link" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

</div>

