
public class duplicate219_1
{
    public static void main(String[] args) {
        int k=3;
        int nums[] = {1,2,3,4,1,6,3};
        System.out.println();
        int flag=0;
        for(int i = 0;i<nums.length-1;i++)
        {
            for(int j=i+1;j<nums.length;j++){
                if(nums[i]==nums[j])
                {
                    if(Math.abs(i-j)<=k)
                    {
                        flag++;
                        break;
                    }
                }
            }
        }
        if(flag!=0)
        System.out.println("True");
        else
        System.out.println("False");
    }
}