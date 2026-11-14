package conjoin

import "strings"

const (
	regionOfKeyWithoutRegionCode = "us"
	apiRootDomain                = "conjoin.cloud"
	keySegmentSeparator          = "_"
)

var (
	keyBasePrefixes = []string{"cak_", "cpk_"}
	keyRegions      = map[string]bool{"us": true, "eu": true, "gh": true}
	keyModes        = map[string]bool{"live": true, "test": true}
)

func keyRegion(key string) string {
	for _, prefix := range keyBasePrefixes {
		rest, found := strings.CutPrefix(key, prefix)
		if !found {
			continue
		}
		segments := strings.SplitN(rest, keySegmentSeparator, 3)
		if len(segments) >= 2 && keyRegions[segments[0]] && keyModes[segments[1]] {
			return segments[0]
		}
		return regionOfKeyWithoutRegionCode
	}
	return regionOfKeyWithoutRegionCode
}

func regionBaseURL(region string) string {
	if region == regionOfKeyWithoutRegionCode {
		return "https://api." + apiRootDomain
	}
	return "https://api." + region + "." + apiRootDomain
}
