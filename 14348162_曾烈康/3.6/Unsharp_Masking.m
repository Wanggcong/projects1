function Unsharp_Masking()
    close all
    fi=imread('Fig3.43(a).jpg');
    figure,imshow(fi),title('原始图像');

    im = double(fi);
    mask = [1/9 1/9 1/9;1/9 1/9 1/9;1/9 1/9 1/9];%mask表示掩模矩阵
    %c=conv2(fi,w,'same');              %可用系统自带的卷积函数实现
    c = BlurFilter(im,mask);
    figure,imshow(c),title('模糊图像');
    imwrite(c,'Fig3.43(a)blur.jpg');
    gmask = im-c;
    figure,imshow(gmask),title('模板图像');
    imwrite(gmask,'Fig3.43(a)mask.jpg');
    
    A=[1,2,3,5,10,20,30,50];                 %A中是随机设置的测试常数
    for i = 1:length(A)
        g = im*(A(i)-1)+gmask;
        g = uint8(g);                   %每次均打印出图像
        figure(i),imshow(g),title(['非锐化图像 A=',num2str(A(i))]);
        saveas(i,['Fig3.43(a)_A',num2str(A(i)),'.jpg']);
    end
    
function imGau = BlurFilter(fi,mask)    %计算滤波后的矩阵
    im = double(fi);
    [m,n] = size(fi);
    imGau = zeros(m,n);
    for x = 2:m-1           %对每个像素点，按掩模矩阵加权求和周围的像素值
        for y = 2:n-1
            imGau(x,y)=im(x-1,y-1)*mask(1,1)+im(x-1,y)*mask(1,2)+im(x-1,y+1)*mask(1,3)...          
                +im(x,y-1)*mask(2,1)+im(x,y)*mask(2,2)+im(x,y+1)*mask(2,3)...        
                +im(x+1,y-1)*mask(3,1)+im(x+1,y)*mask(3,2)+im(x+1,y+1)*mask(3,3);
        end
    end